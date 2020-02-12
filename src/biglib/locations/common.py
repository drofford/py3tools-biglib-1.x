import logging
import os
import os.path
import re
import sys


def find_home_dir():
    home_dir = os.getenv("HOME")
    logging.debug(f'Value of HOME environment variable = "{home_dir}"')

    if home_dir is None or len(home_dir.strip()) == 0:
        return False, ["The HOME environment variable is not defined"]

    if not os.path.exists(home_dir):
        return (
            False,
            [
                f"The HOME environment variable refers to a nonexistent directory: {home_dir}"
            ],
        )

    if not os.path.isdir(home_dir):
        return (
            False,
            [
                f"The HOME environment variable refers to a non-directory item: {home_dir}"
            ],
        )

    return True, os.path.realpath(home_dir)


def find_gradle_properties():

    pass


def find_projects_home_dir():
    pass


def find_interceptas_home_dir():
    pass


def find_vertigo_home_dir():
    pass


def get_a_root_dir(cls, proj_name, prop_name):
    pass
