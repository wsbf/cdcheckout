#!/usr/bin/env python


import sys, os

sys.path.insert(0,os.path.join(os.path.dirname(__file__), './includes'))
import views.mainView
import models.libalbum

class Controller(object):
	def __init__(self):
		self.libalbum = models.libalbum.LibalbumModel()
		self.view = views.mainView.MainView(self)
		self.updateAlbumView()
		self.view.initialize()


	
	def updateAlbumView(self):
		fieldNames = ("Artist","Album")
		albums = self.libalbum.searchByRotation(0) # 0 means to be reviewed
		albumList = [(x[11], x[1]) for x in albums]
		self.view.setAlbumView(fieldNames, albumList)
		
	
if __name__ == "__main__":
	c = Controller()
