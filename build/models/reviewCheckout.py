import db

class ReviewCheckoutModel(db.DatabaseModel):
	def checkout(self, albumID, username):
		print "ReviewCheckoutModel::checkout"
		self.cursor.execute("""INSERT INTO `check_out` (albumID, username)
		VALUES(%s, %s)""", (albumID, username))
	
	def listOutstanding(self, username):
		self.cursor.execute("""SELECT * FROM `check_out` 
			WHERE username LIKE %s""",\
		(username,))
		return self.cursor.fetchall()
