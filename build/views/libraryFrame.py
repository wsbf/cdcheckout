import ttk
import Tkinter as tk
import tkMessageBox
import models.mediums
import libraryController

class LibraryFrame(ttk.Frame):
	def __init__(self, *args, **kw):
		ttk.Frame.__init__(self, *args, **kw)
		
		self.controller = libraryController.LibraryController(self)
		
		albumArtistFrame = ttk.Frame(self)
		albumArtistFrame.grid(column=0, row=0, sticky='nsew', padx=20, pady=20, in_=self)
		albumLabel = ttk.Label(albumArtistFrame, text="Album:")
		albumLabel.grid(column=0,row=0,sticky='e', padx=10, pady=10)
		self.album = ttk.Entry(albumArtistFrame)
		self.album.grid(column=1,row=0,sticky='w', padx=10, pady=10)
		
		artistLabel = ttk.Label(albumArtistFrame, text="Artist:")
		artistLabel.grid(column=0,row=1,sticky='e', padx=10, pady=10)
		self.artist = ttk.Entry(albumArtistFrame)
		self.artist.grid(column=1,row=1,sticky='w', padx=10, pady=10)
		
		m = models.mediums.MediumsModel()
		media = m.list()
		self.mediumID = tk.IntVar()
		self.buttons = []
		self.buttonFrame = ttk.LabelFrame(self, text="Medium:")
		self.buttonFrame.grid(column=1, row=0, sticky='ne', padx=10, pady=10, in_=self)
		for medium in media:
			if medium[1] != "Digital":
				b = ttk.Radiobutton(self.buttonFrame, text=medium[1], variable=self.mediumID, value=int(medium[0]))
			if medium[1] == "CD":
				b.invoke()	## make cd the default option
			b.grid(row=medium[0], sticky='w', in_=self.buttonFrame)
			self.buttons.append(b)
		
	def clearFields(self):
		self.album.delete(0,'end')
		self.artist.delete(0,'end')
		self.buttons[2].invoke()
		
	def confirmCheckout(self):
		if self.artist.get() == "":
			raise Exception("Please enter an artist name.")
		elif self.album.get() == "":
			raise Exception("Please enter an album name.")
		return tkMessageBox.askyesno("Sure?", "Are you sure you want to check out this album?")
	
	def displayCheckoutSuccess(self):
		tkMessageBox.showinfo("Success!", "Successfully checked out \""+self.album.get()+"\" by "+self.artist.get())
