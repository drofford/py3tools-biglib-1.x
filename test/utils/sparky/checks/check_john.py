# import logging

from biglib import logger

logger.debug("sparky :: checks :: check_john.py")


def do():
    logger.debug(f"sparky :: checks :: check_john.py :: do()")
    return True


def description():
    return "This check does whatever John wants!"
