"""
contains the functions necessary to create a pdf file from images

:author: Otavio Sartorelli de Toledo Piza
:version: 2021-06-14
"""

# ======= #
# imports #
# ======= #

from os import scandir, DirEntry, walk
from typing import List, NoReturn, Tuple, Dict


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
        self.images = self.get_images(images_paths)

    def __len__(self) -> int:
        """
        override the length method by returning how many pages the document has

        :return: number of pages in the document
        """
        return self.pages

    # == static methods == #

    @staticmethod
    def images_in_folder(path: str) -> List[str]:
        """
        returns all the images in a folder

        :param path: path to images
        :return:
        """
        img: DirEntry
        return [img.name for img in scandir(path) if img.name.split('.')[-1] in 'jpg jpeg png']

    @staticmethod
    def get_images(paths: List[str]) -> Dict[str, List[str]]:
        """
        returns a dict with all images in the paths provided

        :return:
        """
        folder: Tuple[str, List[str], List[str]]
        return {path[0]: PDF.images_in_folder(path[0]) for image_path in paths
                for path in walk(image_path) if PDF.images_in_folder(path[0])}


if __name__ == '__main__':
    test = PDF(['../test'])
    print(test.images)
