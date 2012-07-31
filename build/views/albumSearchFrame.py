import ttk
import Tkinter as tk

class AlbumSearchFrame(object, tk.Frame):
	"""
	This 'super-widget' (actually a frame containing other widgets) serves as
	a list of albums (in To Be Reviewed) with a search bar that filters
	entries out.
	"""
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		# Construct parent (frame)
		# Set everything apart in a LabelFrame
		frame = self.LabelFrame = ttk.LabelFrame(self, text="Albums To Be Reviewed:")
		frame.grid(column=0, row=0, sticky='nsew')
		
		# album search bar
		self.albumSearchbar = ttk.Entry()
		self.albumSearchbar.grid(column=0, columnspan=3, row=0, sticky='w', in_=frame)
		
		# album list is a Treeview (excellent for tabulated data)
		self.albumList = ttk.Treeview()
		# scrollbar for TreeView	
		vsb = ttk.Scrollbar(orient="vertical", command=self.albumList.yview)
		self.albumList.configure(yscrollcommand=vsb.set)
		# And grid it all 
		self.albumList.grid(column=0, row=1, sticky='nsew', in_=frame)
		vsb.grid(column=1, row=1, sticky='ns', in_=frame)
		frame.grid_columnconfigure(0, weight=1)
		frame.grid_rowconfigure(0, weight=1)
		
	def getSelectedAlbum(self):
		pass
		
	def removeEntry(self):
		pass
		
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
			
			
	def sortby(self, col, descending):
		"""Sort tree contents when a column is clicked on."""
		# grab values to sort
		tree = self.albumList
		data = [(tree.set(child, col), child) for child in tree.get_children('')]

		# reorder data
		data.sort(reverse=descending)
		for indx, item in enumerate(data):
		    tree.move(item[1], '', indx)

		# switch the heading so that it will sort in the opposite direction
		tree.heading(col,
		    command=lambda col=col: self.sortby(col, int(not descending)))
