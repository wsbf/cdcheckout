#!/usr/bin/python
'''This script should be run to start up the app.'''
import sys, os
sys.path.insert(0,os.path.join(os.path.dirname(__file__), './controllers'))
import mainController

if __name__ == "__main__":
	c = mainController.MainController()
	
