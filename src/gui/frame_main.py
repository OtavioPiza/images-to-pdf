from tkinter import Tk, LabelFrame, messagebox, StringVar, Label
from tkinter.filedialog import askdirectory
from tkinter.ttk import Button, Progressbar
from typing import Callable, NoReturn

from src.converter import PDF


class MainFrame(LabelFrame):
    """
    main frame for the images to pdf application
    """

    def __init__(self, root: Tk, do_reset: Callable):
        """
        :param root: tkinter root
        :param do_reset: function to reset the application
        """
        self.do_reset = do_reset

        # == create window == #

        LabelFrame.__init__(self, root)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # == add widgets == #

        self.bt = Button(self, text='Create PDF', command=self.create_pdf)
        self.bt.grid(row=0, column=0, sticky='news')

        self.pb = Progressbar(self, orient='horizontal', mode='determinate', length=1000)
        self.pb.grid(row=1, column=0)

        self.ps_text = StringVar()
        self.ps_text.set(f'Scanning images: {self.pb["value"]:.2f}% complete' if self.pb["value"]
                         else 'select a folder')

        self.label = Label(self, textvariable=self.ps_text)
        self.label.grid(row=2, column=0, sticky='news')

    def create_pdf(self) -> NoReturn:
        """
        creates a new pdf object with the directory provided by the user
        """
        # == ask for directory == #

        path_to_images = askdirectory(title='Select a folder with the images', initialdir='~')

        if not path_to_images:
            return

        # == create pdf == #

        pdf = PDF(path_to_images.split('/')[-1], [path_to_images], '/'.join(path_to_images.split('/')[:-1]), '')
        pdf.add_pages(self.increase_progress_bar)

        self.ps_text.set('Saving the PDF...')
        self.update()

        pdf.create_pdf()
        messagebox.showinfo('Images to PDF', message='PDF created')

        self.do_reset()

    def increase_progress_bar(self, i: int):
        """
        increases the progress bar by i 

        :param i: progress bar increment
        """
        self.pb['value'] += i
        self.ps_text.set(f'Scanning images: {self.pb["value"]:.2f}% complete')
        self.update()
