from tkinter import Tk, messagebox, X, N
from tkinter.filedialog import askdirectory
from typing import NoReturn

from src.converter import PDF
from src.gui.frame_main import MainFrame


class App:
    """
    Class for the image to pdf converter application
    """

    def __init__(self):
        """
        constructor
        """

        # == set up window == #

        self.root = Tk()
        self.root.geometry('200x100')
        self.root.title('Images to PDF')
        self.center = None

        path_to_images = askdirectory(title='Select a folder with the images', initialdir='~')
        pdf = PDF(path_to_images.split('/')[-1], [path_to_images], '/'.join(path_to_images.split('/')[:-1]))
        pdf.create_pdf()

        messagebox.showinfo('Images to PDF', 'PDF created')

    def update_center(self, mode: str = 'main') -> NoReturn:
        """
        updates the center depending on the mode provided

        :param mode: mode
        """
        if self.center:
            self.center.destroy()

        if mode == 'main':
            self.center = MainFrame(self.root, self.update_center)

        else:
            pass

        self.center.pack(padx=10, pady=10, fill=X, anchor=N)


App()
