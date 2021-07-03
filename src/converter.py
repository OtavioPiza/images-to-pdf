"""
contains the functions necessary to create a pdf file from images

:author: Otavio Sartorelli de Toledo Piza
:version: 2021-06-14
"""

# ======= #
# imports #
# ======= #

from typing import List, NoReturn, Union
from PIL import Image
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from os.path import dirname

from src.image_scaner import get_images


# ======= #
# classes #
# ======= #


class PDF:

    # == special methods == #

    def __init__(self, title: str, images_paths: List[str], pdf_path: str = '', author: str = '') -> NoReturn:
        """
        :param images_path: paths to folder with image files
        :param pdf_path: path to save the pdf file
        """
        self.pages = 0
        self.title = title
        self.author = author
        self.pdf_path = '.' if not pdf_path else pdf_path
        self.images = get_images(images_paths)
        self.pdf: Union[None, canvas.Canvas] = None
        self.total = sum(len(self.images[k]) for k in self.images.keys())

    def __len__(self) -> int:
        """
        override the length method by returning how many pages the document has

        :return: number of pages in the document
        """
        return self.pages

    # == methods == #

    def add_pages(self, updater: Union[None, (int)] = None) -> NoReturn:
        self.pdf = canvas.Canvas(f'{self.pdf_path}/{self.title}.pdf')
        self.pdf.setTitle(self.title)
        self.pdf.setAuthor(self.author)

        folders: List[str] = list(self.images.keys())
        folders.sort()

        for folder in folders:
            images_paths: List[str] = self.images[folder]
            images_paths.sort()
            first = True

            for image_path in images_paths:
                self.pages += 1
                path: str = f'{folder}/{image_path}'

                if first:
                    self.pdf.bookmarkPage(path)
                    self.pdf.addOutlineEntry(f'{dirname(path).split("/")[-1]}', path, 0, 0)
                    first = False

                with Image.open(path) as img:
                    self.pdf.setPageSize(img.size)

                self.pdf.drawImage(ImageReader(path), 0, 0, mask='auto')
                self.pdf.showPage()

                if updater:
                    updater(100 / self.total)

    def create_pdf(self) -> NoReturn:
        """
        creates a pdf with the images provided

        :return: number of pages created
        """
        self.pdf.save()
