import db
import user

class LibraryCheckoutModel(db.DatabaseModel):
	def checkOut(self, user, albumName, artistName, mediumID):
		self.cursor.execute("""INSERT INTO `check_out_library` (username, 
		album_name, artist_name, mediumID) VALUES (%s, %s, %s, %s)""",
		(user.username, albumName, artistName, mediumID))
		
	def listOutstanding(self, username):
		self.cursor.execute("""SELECT * FROM `check_out_library` WHERE username
		LIKE %s AND checked_in_date IS NULL""", (username,))
		return self.cursor.fetchall()
		
	
	def checkIn(self, checkOutID):
		import time
		date = time.strftime("%Y-%m-%d %H:%M:%S")
		self.cursor.execute("""UPDATE `check_out_library` SET checked_in_date=%s
		WHERE checkoutID = %s""", (date, checkOutID))
		
if __name__ == "__main__":
	u = user.User()
	u.login("_TestUser", "password")
	lm = LibraryCheckoutModel()
	lm.checkOut(u, "eh", "canada", 0)
