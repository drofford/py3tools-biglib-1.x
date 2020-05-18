"""
This module contains assorted list processing functions.
"""

# import logging
import os
import os.path
import re
import sys

from biglib import logger


class ListUtils:
    @classmethod
    def join(
        cls,
        array,
        /,
        add_and=False,
        quoting=False,
        separator=",",
        oxford=False,
        fancy=False,
    ):
        logger.debug("ListUtils#join: ")
        logger.debug(f"  inputs: {array=}")
        logger.debug(f"  inputs: {add_and=}")
        logger.debug(f"  inputs: {quoting=}")
        logger.debug(f"  inputs: {separator=}")
        logger.debug(f"  inputs: {oxford=}")
        logger.debug(f"  inputs: {fancy=}")

        if array is None or len(array) == 0:
            return ""

        if fancy:
            add_and = True
            quoting = True
            separator = ", "
            oxford = True

        logger.debug("ListUtils#join: ")
        logger.debug(f"  updated 1: {array=}")
        logger.debug(f"  updated 1: {add_and=}")
        logger.debug(f"  updated 1: {quoting=}")
        logger.debug(f"  updated 1: {separator=}")
        logger.debug(f"  updated 1: {oxford=}")
        logger.debug(f"  updated 1: {fancy=}")

        if quoting:
            array = ['"' + str(x) + '"' for x in array]
        else:
            array = [str(x) for x in array]

        logger.debug("ListUtils#join: ")
        logger.debug(f"  updated 2: {array=}")
        logger.debug(f"  updated 2: {add_and=}")
        logger.debug(f"  updated 2: {quoting=}")
        logger.debug(f"  updated 2: {separator=}")
        logger.debug(f"  updated 2: {oxford=}")
        logger.debug(f"  updated 2: {fancy=}")

        logger.debug("ListUtils#join: ")
        if add_and and len(array) > 1:
            txt = separator.join(array[:-1])
            logger.debug(f"  [A] {txt=}")

            if len(array) > 2 and oxford:
                txt += separator
                logger.debug(f"  [A.1] {txt=}")

            conj = "and " if txt.endswith(" ") else " and "
            logger.debug(f"  [B] {conj=}")

            txt += conj + array[-1]
            logger.debug(f"  [C] {txt=}")
        else:
            txt = separator.join(array)
            logger.debug(f"  [D] {txt=}")

        return txt

    @classmethod
    def flatten(cls, arg: list, sort_results=False) -> list:
        """
        This function takes an object graph (really, just a list of lists/tuples of
        lists/tuples etc) and flattens the object graph into a one-dimensional list.
        """

        def helper(result, arg):
            if isinstance(arg, list):
                """
                Code level comment.
                """
                for x in arg:
                    helper(result, x)
            elif isinstance(arg, tuple):
                for x in arg:
                    helper(result, x)
            elif isinstance(arg, set):
                for x in sorted(arg):
                    helper(result, x)
            else:
                result.append(arg)
            return result

        r = helper(list(), arg)
        return sorted(r) if sort_results else r
