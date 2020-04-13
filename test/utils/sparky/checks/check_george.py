import logging

from .base_check import BaseCheck

logging.debug("sparky :: checks :: check_george.py")


def do():
    logging.debug(f"sparky :: checks :: check_george.py :: do()")
    return True


def description():
    return "This checks does whatever George wants!"


def pre(args=None):
    logging.debug(f"sparky :: checks :: check_george.py :: pre()")
    return True


def post(args=None):
    logging.debug(f"sparky :: checks :: check_george.py :: post()")
    return False


class George(BaseCheck):
    def do(self):
        logging.debug(f"sparky :: checks :: check_george.py :: George :: do()")
        return False

    def tell(self):
        return "This check does whatever George wants, but from a class!"
