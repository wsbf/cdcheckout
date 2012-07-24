# David Cohen Main View of the Checkout Screen

import Tkinter as tk
import ttk
import sys


class MainView(object):

    def __init__(self):
        root = self.root = tk.Tk()
        root.title("WSBF CD Checkout System")

        self.labelFrame = ttk.Frame(root)

        wsbflabel = ttk.Label(self.labelFrame, "wsbf-fm")
        checkoutlabel = ttk.Label(self.labelFrame, "cd checkout")

        self.buttonFrame = ttk.Frame(root)
        self.mode = ttk.StringVar()
        toBeReviewed = ttk.Radiobutton(self.buttonFrame, text="To Be Reviewed",\
            variable=self.mode, value='toBeReviewed')
        library = ttk.Radiobutton(self.buttonFrame, text="Library",\
            variable=self.mode, value='library')

        self.albumSearchbar = ttk.Entry(root)

        self.albumListbox = ttk.Listbox(root)

        #http://coverage.livinglogic.de/Demo/tkinter/ttk/treeview_multicolumn.py.html


    def initialize(self):
        self.root.mainloop()