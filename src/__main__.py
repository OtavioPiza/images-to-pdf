from tkinter import Tk, X, N
from typing import NoReturn


class App:

    def __init__(self):
        """
        constructor
        """
        self.root = Tk()
        self.root.geometry('200X150')
        self.root.title('Images to PDF')
        self.center = None

    # == methods == #

    def update_center(self, mode: str = 'main') -> NoReturn:
        """
        updates the center depending on the mode provided

        :param mode: mode
        """
        if self.center:
            self.center.destroy()

        if mode == 'main':
            pass

        else:
            pass

        self.center.pack(padx=10, pady=10, fill=X, anchor=N)

