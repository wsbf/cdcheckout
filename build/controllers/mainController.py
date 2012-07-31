import sys, os

sys.path.insert(0,os.path.join(os.path.dirname(__file__), './includes'))
import views.mainView
import models.libalbum
import models.user
import models.reviewCheckout
import reviewController


class MainController(object):
	def __init__(self):
		self.libalbum = models.libalbum.LibalbumModel()
		self.view = views.mainView.MainView(self)
		self.updateAlbumView()
		self.view.initialize()

	
	def updateAlbumView(self):
		fieldNames = ("AlbumID", "Artist","Album")
		self.albums = self.libalbum.listAvailableToBeReviewed() 
#		albumList = [() for x in self.albums]
		self.view.setAlbumView(fieldNames, self.albums)
	
	def login(self):
		self.user = models.user.User()
		self.user.login(str(self.view.loginFrame.username.get()), str(self.view.loginFrame.password.get()))

	def checkout(self, checkoutController):
		self.login()
		print "In checkoutAlbum"
		checkoutController.checkout(self.user.username)
#		 returns a string starting with I followed by hex
#		hexString = selection[0][1:]
#		print "hexString",hexString
#		selectedAlbum = int(hexString, 16) - 1
#		albumID = self.albums[selectedAlbum][0]
#		print "selectedAlbum:", selectedAlbum
#		print "This album is", self.albums[selectedAlbum]
#		rc = models.reviewCheckout.ReviewCheckoutModel()
#		rc.checkOut(albumID, self.user.username)
		


if __name__ == "__main__":
	c = Controller()
