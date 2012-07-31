import sys, os

sys.path.insert(0,os.path.join(os.path.dirname(__file__), './includes'))
import views.mainView
import models.libalbum
import models.user
import models.reviewCheckout
import reviewController


class MainController(object):
	def __init__(self):
		self.view = views.mainView.MainView(self)
		self.view.initialize()
	
	def login(self):
		self.user = models.user.User()
		self.user.login(str(self.view.loginFrame.username.get()), str(self.view.loginFrame.password.get()))

	def checkout(self, checkoutController):
		print "MainController::checkout"
		self.login()
		print "User has logged in:", self.user.username
		# call the checkout function in its controller (whichever it may be)
		checkoutController.checkout(self.user.username)

if __name__ == "__main__":
	c = Controller()
