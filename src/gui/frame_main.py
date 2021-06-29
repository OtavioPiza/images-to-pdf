from tkinter import Tk, LabelFrame, messagebox
from tkinter.filedialog import askdirectory
from tkinter.ttk import Button
from typing import NoReturn

from src.converter import PDF


class MainFrame(LabelFrame):

    def __init__(self, root: Tk, do_reset: ()):
        LabelFrame.__init__(self, root)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.do_reset = do_reset

        Button(self, text='Create PDF', command=self.create_pdf).grid(row=1, column=0, sticky='news')

    def create_pdf(self) -> NoReturn:
        path_to_images = askdirectory(title='Select a folder with the images', initialdir='~')

        pdf = PDF(path_to_images.split('/')[-1], [path_to_images], '/'.join(path_to_images.split('/')[:-1]), '')
        pdf.create_pdf()
        messagebox.showinfo('Images to PDF', message='PDF created')
        self.do_reset()
