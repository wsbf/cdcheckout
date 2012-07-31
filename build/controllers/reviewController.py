''' Acts as a controller for the reviewFrame. However, it is actually created
by the reviewFrame itself (in the constructor). The main purpose of this is 
to properly handle checking out albums.'''

import models.libalbum
import models.reviewCheckout

class ReviewController(object):
	def __init__(self, reviewFrame):
		self.reviewFrame = reviewFrame
		self.libalbum = models.libalbum.LibalbumModel()
		self.albums = self.libalbum.listAvailableToBeReviewed() 

	def update(self):
		fieldNames = ("AlbumID", "Artist","Album")
		self.reviewFrame.setAlbumView(fieldNames, self.albums)

	
	def checkout(self, username):
		album = self.reviewFrame.getSelectedAlbum()
		albumID = int(album[0])
		print "ReviewController::checkout, albumID=",albumID
		rcm = models.reviewCheckout.ReviewCheckoutModel()
		rcm.checkout(albumID, username)
		self.reviewFrame.removeSelectedAlbum()
		self.reviewFrame.displayCheckoutSuccess(album)
