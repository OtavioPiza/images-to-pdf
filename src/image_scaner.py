"""
file with function for scanning for images

:author: Otavio Sartorelli de Toledo Piza
:version: 2021-06-14
"""

# ======= #
# imports #
# ======= #

from os import walk, scandir, DirEntry
from typing import List, Dict, Tuple


# ========= #
# functions #
# ========= #


def images_in_folder(path: str) -> List[str]:
    """
    returns all the images in a folder

    :param path: path to images
    :return:
    """
    img: DirEntry
    return [img.name for img in scandir(path) if img.name.split('.')[-1] in 'jpg jpeg png']


def get_images(paths: List[str]) -> Dict[str, List[str]]:
    """
    returns a dict with all images in the paths provided

    :param paths: paths where images will be searched for
    :return:
    """
    folder: Tuple[str, List[str], List[str]]
    return {path[0]: images_in_folder(path[0]) for image_path in paths
            for path in walk(image_path) if images_in_folder(path[0])}
