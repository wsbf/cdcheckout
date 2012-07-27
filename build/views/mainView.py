"""
David Cohen
This is the main view of the CD Checkout module. 
"""

import Tkinter as tk
import sys, os
sys.path.insert(0,os.path.join(os.path.dirname(__file__), './includes'))
import ttk
import tkMessageBox
#import sys


class MainView(object):

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
		self.loginFrame.grid(column=0, row=0, columnspan=4, sticky='nw')
		self.loginFrame.username = ttk.Entry()
		self.loginFrame.username.grid(column=0, row=0, in_=self.loginFrame, sticky='nsew')
#		self.loginFrame.username.bind("<Button-1>", lambda e: e.widget.textvariable.set(""))
		self.loginFrame.password = ttk.Entry(show="*")
		self.loginFrame.password.grid(column=0, row=1, in_=self.loginFrame,sticky='nsew')
#		self.loginFrame.password.bind("<Button-1>", lambda e: e.widget.config(text=""))
#		self.loginFrame.button = ttk.Button(text="Login", command=self.controller.login)
#		self.loginFrame.button.grid(column=0,row=2, in_=self.loginFrame, sticky='ew')

		####### Library / To Be Reviewed Radio Buttons #######
		self.buttonFrame = buttonFrame = ttk.LabelFrame(root, text="Checking out from:")
		buttonFrame.grid(column=4, row=2, columnspan=2)
		self.mode = tk.StringVar()
		self.toBeReviewed = ttk.Radiobutton(buttonFrame, text="To Be Reviewed",\
			variable=self.mode, value='toBeReviewed')
		self.toBeReviewed.grid(row=0, sticky='w')
		self.library = ttk.Radiobutton(buttonFrame, text="Library",\
			variable=self.mode, value='library')
		self.library.grid(row=1, sticky='w')


		####### Album List Search  #######
		self.albumListFrame = ttk.LabelFrame(root, text="Albums To Be Reviewed:")
		self.albumListFrame.grid(column=0, row=3, columnspan=6, sticky='nsew', in_=root)
		self.albumSearchbar = ttk.Entry()
		self.albumSearchbar.grid(column=0, columnspan=2, row=0, sticky='w', in_=self.albumListFrame)
		self.albumList = ttk.Treeview()
		vsb = ttk.Scrollbar(orient="vertical", command=self.albumList.yview)
		self.albumList.configure(yscrollcommand=vsb.set)
		self.albumList.grid(column=0, row=1, sticky='nsew', in_=self.albumListFrame)
		vsb.grid(column=1, row=1, sticky='ns', in_=self.albumListFrame)
		self.albumListFrame.grid_columnconfigure(0, weight=1)
		self.albumListFrame.grid_rowconfigure(0, weight=1)
		
		#http://coverage.livinglogic.de/Demo/tkinter/ttk/treeview_multicolumn.py.html'

		###### Check Out Button ######
		def tryCheckout():
			if self.albumList.selection() == "":
				tkMessageBox.showerror("What album?", "Select an album to check out.")
			elif tkMessageBox.askyesno("Sure?", "Are you sure you want to check out this album?"):
				try:
					self.controller.checkoutAlbum(self.albumList.selection())
				except Exception, e:
					tkMessageBox.showerror("Failure.", e)
				else:
					tkMessageBox.showinfo("Success!", "Album Successfully Checked Out!")
		self.checkOutButton = ttk.Button(text="Check Out Selected Album!", command=tryCheckout)
		self.checkOutButton.grid(column=0, columnspan=2, row=2, in_=self.root, sticky='ew')

	def initialize(self):
		self.root.mainloop()

	def setAlbumView(self, columns, entries):
		self.albumList.config(columns=columns, show="headings")
		for col in columns:
			self.albumList.heading(col, text=col.title(),
				command=lambda c=col: sortby(self.albumList, c, 0))
			self.albumList.column(col, width=400)

		for item in entries:
			print "Inserting item:", item
			self.albumList.insert('', 'end', values=item)

###################################################
### TODO: Put this sort-by thing somewhere else.
### Figure out how to sort by albumID.
###################################################
def sortby(tree, col, descending):
    """Sort tree contents when a column is clicked on."""
    # grab values to sort
    data = [(tree.set(child, col), child) for child in tree.get_children('')]

    # reorder data
    data.sort(reverse=descending)
    for indx, item in enumerate(data):
        tree.move(item[1], '', indx)

    # switch the heading so that it will sort in the opposite direction
    tree.heading(col,
        command=lambda col=col: sortby(tree, col, int(not descending)))


if __name__ == "__main__":
	v = MainView()
	v.initialize()
