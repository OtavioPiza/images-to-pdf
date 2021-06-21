from tkinter import Tk, LabelFrame
from tkinter.ttk import Button


class MainFrame(LabelFrame):

    def __init__(self, root: Tk, select_folder, create_pdf, **kw):
        LabelFrame.__init__(self, root)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        Button(self, text='Choose Folder', command=select_folder).grid(row=0, column=0, sticky='news')
        Button(self, text='Create PDF', command=create_pdf).grid(row=1, column=0, sticky='news')

