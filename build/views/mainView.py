import Tkinter as tk
import sys, os
sys.path.insert(0,os.path.join(os.path.dirname(__file__), '../includes'))
sys.path.insert(0,os.path.join(os.path.dirname(__file__), '../controllers'))
import ttk
import tkMessageBox

import reviewFrame, libraryFrame

class MainView(object):
	"""
	David Cohen
	This is the main view of the CD Checkout module. 
	"""
	def __init__(self, controller):
		self.controller = controller
		root = self.root = tk.Tk()
		root.title("WSBF CD Checkout System")

		####### MAIN LABELS ######
		self.labelFrame = tk.Frame(root)
		self.labelFrame.grid(column=4, row=0, sticky='nsew')
		self.wsbflabel = tk.Label(self.labelFrame, text="wsbf-fm")
		self.wsbflabel.grid(column=0, row=0, sticky='e')
		self.checkoutlabel = tk.Label(self.labelFrame, text="cd checkout")
		self.checkoutlabel.grid(column=0, row=1, sticky='e')

		###### Login Frame ######
		self.loginFrame = ttk.LabelFrame(root, text="Login Credentials")
		self.loginFrame.grid(column=0, row=0, columnspan=2, padx=10, pady=10, sticky='sw')
		self.loginFrame.username = ttk.Entry()
		self.loginFrame.username.insert(0,"Username")
		self.loginFrame.username.grid(column=0, row=0, in_=self.loginFrame, sticky='nsew')
		self.loginFrame.username.bind("<Button-1>", lambda e: e.widget.delete(0, 'end'))
		self.loginFrame.password = ttk.Entry(show="*")
		self.loginFrame.password.insert(0,"Password")
		self.loginFrame.password.grid(column=0, row=1, in_=self.loginFrame,sticky='nsew')
		self.loginFrame.password.bind("<Button-1>", lambda e: e.widget.delete(0, 'end'))

		######## Album Search / Library -- Notebook #######

		self.notebook = ttk.Notebook(root)		
		
		self.reviewFrame = reviewFrame.ReviewFrame(self.notebook)		
		self.libraryFrame = libraryFrame.LibraryFrame(self.notebook)
		
		# dictionary of tab tuples --- (object, name)
		self.tabs = [(self.reviewFrame, "To Be Reviewed"),(self.libraryFrame, "Library")]
		for tab in self.tabs:
			self.notebook.add(tab[0], text=tab[1])
		self.notebook.grid(column=0, row=3, columnspan=6, sticky='nsew', in_=root)	
		
		# the following line maps the setAlbumView function to the reviewFrame's
		self.setAlbumView = self.reviewFrame.setAlbumView
		

		#http://coverage.livinglogic.de/Demo/tkinter/ttk/treeview_multicolumn.py.html'

		###### Check Out Button ######
		def tryCheckout():
			print "Selected:", self.notebook.tab('current', 'text')
			print "Index:", self.notebook.index('current')
			# currFrame is one of self.[reviewFrame, libraryFrame]
			currFrame = self.tabs[self.notebook.index('current')][0]
			
			try:
				if currFrame.confirmCheckout():	# "are you sure?"
					self.controller.checkout(currFrame.controller)
			except Exception, e:
				tkMessageBox.showerror("Failure.", e)
		
		
		self.checkOutButton = ttk.Button(text="Check Out Item!", command=tryCheckout)
		self.checkOutButton.grid(column=0, columnspan=2, row=2, in_=self.root, sticky='ew')

	def initialize(self):
		self.root.mainloop()






if __name__ == "__main__":
	v = MainView()
	v.initialize()
