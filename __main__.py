from tkinter import Tk, X, N
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
        self.root.withdraw()

        path_to_images = askdirectory(title='Select a folder with the images')
        pdf = PDF(path_to_images.split('/')[-1], [path_to_images], '/'.join(path_to_images.split('/')[:-1]))
        pdf.create_pdf()


App()
