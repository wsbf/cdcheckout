import sys, os, inspect
import unittest
import time
os.path.join(os.path.dirname(__file__), '../models')
sys.path.insert(0,os.path.join(os.path.dirname(__file__), '../models'))
import db
import libraryCheckout
import user

def printFuncName():
    print "==========", inspect.stack()[1][3], "=========="


class TestLibraryCheckout(unittest.TestCase):
	def setUp(self):
		printFuncName()
		self.user = user.User()
		self.user.login("_TestUser", "password")
		self.dbm = db.DatabaseModel()
		self.conn = db.DatabaseModel.conn	# just a shortcut
		self.lc = libraryCheckout.LibraryCheckoutModel()
		self.insertedRows = []	# keep track of rows inserted
		self.checkedInRows = []
	def tearDown(self):
		printFuncName()
		print "Removing test rows:", self.insertedRows
		self.dbm.cursor.executemany("""DELETE FROM `check_out_library` WHERE checkoutID = %s""", self.insertedRows)
		insertedRows = []

	def testCheckOut(self):
		printFuncName()
		beforeRows = self.getNumRows()
		expectedRows = beforeRows + 1
		self.lc.checkOut(self.user, "TestAlbum", "TestArtist", 0)
		self.insertedRows.append(self.conn.insert_id())
		self.assertEqual(expectedRows, self.getNumRows())
	
	def testListOutstanding(self):
		printFuncName()
		self.lc.checkOut(self.user, "testListOutstanding", "listOutstanding", 0)
		self.insertedRows.append(self.conn.insert_id())
		out = self.lc.listOutstanding(self.user.username)
		self.assertEqual(out[-1][1], self.user.username)
		self.assertEqual(out[-1][2], "testListOutstanding")
		self.assertEqual(out[-1][3], "listOutstanding")
		self.assertEqual(out[-1][4], 0)

		print "testListOutstanding :: Making sure all inserted rows are",\
		"marked as outstanding:"
		for index in self.insertedRows:
			try:	# if it was inserted but checked in skip
				if self.checkedInRows.index(index):
					pass
			except:
				foundRow = None
				for row in out:
					if row[0] == index:
						foundRow = row
						print "Found index", index, ":", row
						break
				self.assertNotEqual(foundRow, None)
		
				
	def testCheckIn(self):
		printFuncName()
		beforeOutstanding = self.lc.listOutstanding(self.user.username)
		beforeNumOutstanding = len(beforeOutstanding)
		print "Before Checkout:", beforeOutstanding, "\n"
		self.lc.checkOut(self.user, "testCheckOut", "checkOut", 0)
		self.insertedRows.append(self.conn.insert_id())
		
		duringOutstanding = self.lc.listOutstanding(self.user.username)
		duringNumOutstanding = len(duringOutstanding)
		print "Just checked out:", duringOutstanding, "\n"

		self.assertEqual(beforeNumOutstanding+1, duringNumOutstanding)
		self.lc.checkIn(duringOutstanding[-1][0])
		self.checkedInRows.append(self.conn.insert_id())
		afterOutstanding = self.lc.listOutstanding(self.user.username)
		afterNumOutstanding = len(afterOutstanding)
		print "Checked back in:", afterOutstanding, "\n"
		self.assertEqual(beforeNumOutstanding, afterNumOutstanding)

	
	def getNumRows(self):
		self.dbm.cursor.execute("""SELECT COUNT(*) FROM `check_out_library` WHERE
			username = %s""", self.user.username)
		res = self.dbm.cursor.fetchone()[0]
		print "User", self.user.username, "has", res, \
			"albums checked out from the library."
		return res

if __name__ == "__main__":
	unittest.main()
