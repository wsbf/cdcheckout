import db
import hashlib

class User(db.DatabaseModel):
	def __init__(self):
		# construct superclass
		super(User, self).__init__()
		self.username = None
		self.name = None
		self._passwordMD5 = None
		
	def login(self, username, password):
		self._passwordMD5 = hashlib.md5(password).hexdigest()
		self.cursor.execute("""SELECT password, preferred_name FROM users
			WHERE username LIKE %s LIMIT 1""", (username,))		
		userEntry = self.cursor.fetchone()

		if not userEntry:
			raise Exception("User " +username+" not found.")
		salt = userEntry[0][:64]
		answer = userEntry[0][64:]
		if hashlib.sha512( salt + self._passwordMD5).hexdigest() != answer:
			raise Exception("Incorrect Password.")

		print "User logged in:",username
		self.username = username
		self.name = userEntry[1]
	
