from tkinter import Tk, LabelFrame
from tkinter.filedialog import askdirectory
from tkinter.simpledialog import askstring
from tkinter.ttk import Button
from typing import NoReturn

from src.converter import PDF


class MainFrame(LabelFrame):

    def __init__(self, root: Tk):
        LabelFrame.__init__(self, root)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        Button(self, text='Create PDF', command=self.create_pdf).grid(row=1, column=0, sticky='news')

    @staticmethod
    def create_pdf() -> NoReturn:
        author = askstring('Images to PDF', 'Who is the author of the pdf?')
        path_to_images = askdirectory(title='Select a folder with the images')
        path_to_pdf = askdirectory(title='Select a location to save the pdf')

        pdf = PDF(path_to_images.split('/')[-1], [path_to_images], path_to_pdf, author)
        pdf.create_pdf()
