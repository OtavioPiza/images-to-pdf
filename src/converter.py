'''
contains the functions necessary to create a pdf file from images

:author: Otavio Sartorelli de Toledo Piza
:version: 2021-06-14
'''

# ======= #
# imports #
# ======= #

from typing import List, NoReturn, Union

# ======= #
# classes #
# ======= #


class PDF:

    def __init__(self, images_paths: List[str], pdf_path: str = '') -> NoReturn:
        '''
        :param images_path: paths to folder with image files
        :param pdf_path: path to save the pdf file
        '''
        self.pages = 0
        self.images_paths = images_paths
        self.pdf_path = 'pdf' if not pdf_path else pdf_path
