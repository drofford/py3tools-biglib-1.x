# import logging

from biglib import logger

logger.debug("sparky :: checks :: check_paul.py")


def do():
    logger.debug(f"sparky :: checks :: check_paul.py :: do()")
    return True


def _description():
    return "This check does whatever Paul wants!"
