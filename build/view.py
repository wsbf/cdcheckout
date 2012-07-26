# David Cohen Main View of the Checkout Screen

import Tkinter as tk
#import ttk
#import sys


class MainView(object):

    def __init__(self):
        root = self.root = tk.Tk()
        root.title("WSBF CD Checkout System")
        #self.labelFrame = ttk.Frame(root)

        self.wsbflabel = tk.Label(root, text="wsbf-fm")
        self.wsbflabel.grid(column=4, row=0, sticky=tk.E)
        self.checkoutlabel = tk.Label(root, text="cd checkout")
        self.checkoutlabel.grid(column=4, row=1, sticky=tk.E)

        self.buttonFrame = buttonFrame = tk.Frame(root)
        self.mode = tk.StringVar()
        self.toBeReviewed = tk.Radiobutton(buttonFrame, text="To Be Reviewed",\
            variable=self.mode, value='toBeReviewed')
        self.toBeReviewed.grid(row=0)
        self.library = tk.Radiobutton(buttonFrame, text="Library",\
            variable=self.mode, value='library')
        self.library.grid(row=1)

        self.albumSearchbar = tk.Entry(root)
        self.albumSearchbar.grid(column=0, columnspan=2, row=2, sticky=tk.E + tk.W)
        self.albumListbox = tk.Listbox(root)
        self.albumListbox.grid(column=0, row=3, columnspan=6, sticky=tk.N + tk.S + tk.E + tk.W)

        #http://coverage.livinglogic.de/Demo/tkinter/ttk/treeview_multicolumn.py.html
    def initialize(self):
        self.root.mainloop()

if __name__ == "__main__":
    v = MainView()
    v.initialize()
