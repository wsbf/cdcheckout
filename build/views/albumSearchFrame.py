"""
This 'super-widget' (actually a frame containing other widgets) serves as
a list of albums (in To Be Reviewed) with a search bar that filters
entries out.
"""
import ttk
import Tkinter as tk

class AlbumSearchFrame(object, ttk.Frame):
	def __init__(self, parent):
		####### Album List Search  #######
		self.albumListFrame = ttk.LabelFrame(root, text="Albums To Be Reviewed:")
		self.albumListFrame.grid(column=0, row=3, columnspan=6, sticky='nsew', in_=root)
		self.albumSearchbar = ttk.Entry()
		self.albumSearchbar.grid(column=0, columnspan=2, row=0, sticky='e', in_=self.albumListFrame)
		self.albumList = ttk.Treeview()
		vsb = ttk.Scrollbar(orient="vertical", command=self.albumList.yview)
		self.albumList.configure(yscrollcommand=vsb.set)
		self.albumList.grid(column=0, row=1, sticky='nsew', in_=self.albumListFrame)
		vsb.grid(column=1, row=1, sticky='ns', in_=self.albumListFrame)
		self.albumListFrame.grid_columnconfigure(0, weight=1)
		self.albumListFrame.grid_rowconfigure(0, weight=1)