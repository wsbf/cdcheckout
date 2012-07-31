import models.libraryCheckout

class LibraryController(object):
	def __init__(self, libraryFrame):
		self.frame = libraryFrame
		self.model = models.libraryCheckout.LibraryCheckoutModel()
	
	def checkout(self, username):
		album = self.frame.album.get()
		artist = self.frame.artist.get()
		mediumID = self.frame.mediumID.get()
		self.model.checkout(username, album, artist, mediumID)
		self.frame.displayCheckoutSuccess()
		self.frame.clearFields()

