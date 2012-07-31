import ttk
import Tkinter as tk
import tkMessageBox
import re
import controllers.reviewController

class ReviewFrame(ttk.Frame):
	"""
	This 'super-widget' (actually a frame containing other widgets) serves as
	a list of albums (in To Be Reviewed) with a search bar that filters
	entries out.
	"""
	def __init__(self, *args, **kw):
		ttk.Frame.__init__(self, *args, **kw)
		self.controller = controllers.reviewController.ReviewController(self)

		# album search bar
		self.albumSearchbar = ttk.Entry()
		self.albumSearchbar.insert(0, "Search for an album...")
		self.albumSearchbar.bind("<FocusIn>", lambda e: e.widget.delete(0,'end'))
		self.albumSearchbar.bind("<KeyRelease>", lambda e: self.filterResults())
		self.albumSearchbar.bind("<KeyRelease-BackSpace>", lambda e: self.unFilterResults())
		self.albumSearchbar.grid(column=0, columnspan=3, row=0, sticky='w', padx=10, pady=10, in_=self)
		
		self.removedResults = []
		
		# album list is a Treeview (excellent for tabulated data)
		self.albumList = ttk.Treeview()
		# scrollbar for TreeView	
		vsb = ttk.Scrollbar(orient="vertical", command=self.albumList.yview)
		self.albumList.configure(yscrollcommand=vsb.set)
		# And grid it all 
		self.albumList.grid(column=0, row=1, sticky='nsew', in_=self)
		vsb.grid(column=1, row=1, sticky='ns', in_=self)
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=1)

		self.controller.update()

	def getSelectedAlbum(self):	
		return(self.albumList.item(self.albumList.selection(), 'values'))
		
	def removeSelectedAlbum(self):
		self.albumList.delete(self.albumList.selection())
	
	################################################################
	######### Search / Filter functionality ########################
	def filterResults(self):
		'''Called whenever a character is entered into albumSearchbar. Removes
		anything that doesn't match'''
		print "ReviewFrame :: filterResults"
		searchString = self.albumSearchbar.get()
		for item in self.albumList.get_children():
			vals = self.albumList.item(item, 'values')
			if not (re.search(searchString, vals[0], re.IGNORECASE) or re.search(searchString, vals[1],re.IGNORECASE) or re.search(searchString, vals[2], re.IGNORECASE)):
				self.removedResults.append((item, self.albumList.parent(item), self.albumList.index(item)))
				self.albumList.detach(item)

	def unFilterResults(self):
		'''Called when backspace is pressed. Adds back entries that match again'''
		print "ReviewFrame :: unFilterResults"
		searchString = self.albumSearchbar.get()
		for entry in reversed(self.removedResults):
			vals = self.albumList.item(entry[0], 'values')
			if (re.search(searchString, vals[0], re.IGNORECASE) or re.search(searchString, vals[1],re.IGNORECASE) or re.search(searchString, vals[2], re.IGNORECASE)):
				print "\tfound match:",vals
				self.albumList.reattach(entry[0], entry[1], entry[2])
			del entry
	
	##############################################
	########## Initial setup #####################
	def setAlbumView(self, columns, entries):
		self.albumList.config(columns=columns, show="headings")
		for col in columns:
			self.albumList.heading(col, text=col.title(),
				command=lambda c=col: self.sortby(c, 0))
			self.albumList.column(col, width=400)
		self.albumList.column(columns[0], width=60)
		for item in entries:
			print "Inserting item:", item
			self.albumList.insert('', 'end', values=item)
	
	def confirmCheckout(self):
		if self.albumList.selection() == "":
			raise Exception("No album selected.")
		return tkMessageBox.askyesno("Sure?", "Are you sure you want to check out this album?")
	
	def displayCheckoutSuccess(self, album):
		tkMessageBox.showinfo("Success!", "Successfully checked out \""+album[1]+"\" by "+album[2])
		
			
	def sortby(self, col, descending):
		"""Sort tree contents when a column is clicked on."""
		# grab values to sort
		print "sorting, col:", col
		tree = self.albumList
		# we need to sort as ints if it's the albumID
		if col == "AlbumID":
			data = [(int(tree.set(child, col)), child) for child in tree.get_children('')]
		else:
			data = [(tree.set(child, col), child) for child in tree.get_children('')]

		# reorder data
		data.sort(reverse=descending)
		for indx, item in enumerate(data):
		    tree.move(item[1], '', indx)

		# switch the heading so that it will sort in the opposite direction
		tree.heading(col,
		    command=lambda col=col: self.sortby(col, int(not descending)))
