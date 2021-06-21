"""
contains the functions necessary to create a pdf file from images

:author: Otavio Sartorelli de Toledo Piza
:version: 2021-06-14
"""

# ======= #
# imports #
# ======= #

from typing import List, NoReturn
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

    def __len__(self) -> int:
        """
        override the length method by returning how many pages the document has

        :return: number of pages in the document
        """
        return self.pages

    # == methods == #

    def create_pdf(self) -> NoReturn:
        """
        creates a pdf with the images provided

        :return: number of pages created
        """
        pdf = canvas.Canvas(f'{self.pdf_path}/{self.title}.pdf')
        pdf.setTitle(self.title)
        pdf.setAuthor(self.author)

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
                    pdf.bookmarkPage(path)
                    pdf.addOutlineEntry(f'{dirname(path).split("/")[-1]}', path, 0, 0)
                    first = False

                with Image.open(path) as img:
                    pdf.setPageSize(img.size)

                pdf.drawImage(ImageReader(path), 0, 0, mask='auto')
                pdf.showPage()

        pdf.save()
