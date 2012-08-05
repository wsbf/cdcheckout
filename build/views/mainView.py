import Tkinter as tk
import sys, os
sys.path.insert(0,os.path.join(os.path.dirname(__file__), '../includes'))
sys.path.insert(0,os.path.join(os.path.dirname(__file__), '../controllers'))
import ttk
import tkMessageBox
import tkFont
import reviewFrame, libraryFrame

class MainView(object):
	"""
	David Cohen
	This is the main view of the CD Checkout module. 
	"""
	def __init__(self, controller):
		self.controller = controller
		root = self.root = tk.Tk()
		self._geom='1024x800+0+0'
		self.SCREEN_HEIGHT = self.root.winfo_screenheight()
		self.SCREEN_WIDTH = self.root.winfo_screenwidth()
		self.pad = 15
		root.bind("<Escape>", lambda e: sys.exit())
		root.title("WSBF CD Checkout System")
		root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
#		root.overrideredirect(True)
		root.attributes('-topmost', True)

		self.makeLabels()	
		
		self.makeLoginFrame()

		######## Album Search / Library -- Notebook #######

		self.notebook = ttk.Notebook(root, width=self.SCREEN_WIDTH-self.pad, height=self.SCREEN_HEIGHT/2)

		self.reviewFrame = reviewFrame.ReviewFrame(self.notebook, height=self.SCREEN_HEIGHT/2)		
		self.libraryFrame = libraryFrame.LibraryFrame(self.notebook)
		
		# dictionary of tab tuples --- (object, name)
		self.tabs = [(self.reviewFrame, "To Be Reviewed"),(self.libraryFrame, "Library")]
		for tab in self.tabs:
			self.notebook.add(tab[0], text=tab[1])
		self.notebook.grid(column=0, row=3, columnspan=5, sticky='nsew', in_=root)	
		
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
					if tkMessageBox.askyesno(message="Would you like to log out?",\
					title='Log out?',icon='question'):
						self.controller.logout()
						
			except Exception, e:
				tkMessageBox.showerror("Failure.", e)
		
		
		self.checkOutButton = ttk.Button(text="Check Out Item!", command=tryCheckout)
		self.checkOutButton.grid(column=0, columnspan=2, row=2, in_=self.root, sticky='ew')

	def initialize(self):
		self.root.mainloop()

	def makeLoginFrame(self):
		###### Login Frame ######
		self.loginFrame = ttk.LabelFrame(self.root, text="Login Credentials")
		self.loginFrame.grid(column=0, row=0, columnspan=2, padx=10, pady=10, sticky='sw')
		self.loginFrame.username = ttk.Entry()
		
		self.loginFrame.username.grid(column=0, row=0, in_=self.loginFrame, sticky='nsew')
		self.loginFrame.username.bind("<Button-1>", lambda e: e.widget.delete(0, 'end'))
		self.loginFrame.password = ttk.Entry(show="*")
		
		self.loginFrame.password.grid(column=0, row=1, in_=self.loginFrame,sticky='nsew')
		self.loginFrame.password.bind("<Button-1>", lambda e: e.widget.delete(0, 'end'))
		self.resetUser()
		
	def resetUser(self):
		self.loginFrame.username.delete(0,tk.END)
		self.loginFrame.password.delete(0,tk.END)
		self.loginFrame.username.insert(0,"Username")
		self.loginFrame.password.insert(0,"Password")
	
	def makeLabels(self):
		####### MAIN LABELS ######
		labelFont = tkFont.Font(family='Helvetica', size='24', weight='bold')
		self.labelFrame = tk.Frame(self.root)
		self.labelFrame.grid(column=4, row=0, sticky='nsew',in_=self.root)
		wsbflabel = ttk.Label(self.labelFrame, text="wsbf-fm", font=labelFont)
		wsbflabel.grid(column=0, row=0, sticky='se',in_=self.labelFrame)
		checkoutlabel = ttk.Label(self.labelFrame, text="cd checkout", font=labelFont)
		checkoutlabel.grid(column=0, row=1, sticky='ne',in_=self.labelFrame)

		self.ladypi = tk.PhotoImage(file="includes/img/wsbflady.gif")
		ladyLabel = tk.Label(self.labelFrame, image=self.ladypi, width=250, height=250)
		ladyLabel.image = self.ladypi
		ladyLabel.grid(column=1, row=0, rowspan=2, sticky='nsew', in_=self.labelFrame)
if __name__ == "__main__":
	v = MainView()
	v.initialize()
