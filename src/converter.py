"""
contains the functions necessary to create a pdf file from images

:author: Otavio Sartorelli de Toledo Piza
:version: 2021-06-14
"""

# ======= #
# imports #
# ======= #

from typing import List, NoReturn

from src.image_scaner import get_images


# ======= #
# classes #
# ======= #


class PDF:

    # == special methods == #

    def __init__(self, images_paths: List[str], pdf_path: str = '') -> NoReturn:
        """
        :param images_path: paths to folder with image files
        :param pdf_path: path to save the pdf file
        """
        self.pages = 0
        self.pdf_path = 'pdf' if not pdf_path else pdf_path
        self.images = get_images(images_paths)

    def __len__(self) -> int:
        """
        override the length method by returning how many pages the document has

        :return: number of pages in the document
        """
        return self.pages


if __name__ == '__main__':
    test = PDF(['../test'])
    print(test.images)
