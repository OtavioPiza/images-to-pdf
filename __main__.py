"""
main file for the images to pdf application

:version: 2021.07.04
:author: Otavio Sartorelli de Toledo Piza
"""

# ======= #
# imports #
# ======= #

from tkinter import Tk, X, N
from typing import NoReturn

from src.gui.frame_main import MainFrame

# ======= #
# classes #
# ======= #


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
        self.root.geometry('400x90')
        self.root.title('Images to PDF')
        self.center = None

        self.update_center()

        self.root.mainloop()

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
