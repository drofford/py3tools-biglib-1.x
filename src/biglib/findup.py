import argparse
import os
import os.path
import sys

import daiquiri
from biglib import logger

DEPTH = 100
depth = 0


def findup(folder, entry):
    def _find(folder, entry, previous=None):
        global depth
        logger.debug("Testing: dir={} for file={}".format(folder, entry))
        logger.debug("    prev dir={}".format(previous))
        if folder == previous:
            logger.debug(
                "Reached top of file system - file not found: {}".format(entry)
            )
            return False, ['Not found: "%s"' % entry]

        f = os.path.realpath(os.path.join(folder, entry))
        logger.debug("testing {}".format(f))
        if os.path.exists(entry) or os.path.isfile(f) or os.path.isdir(f):
            logger.debug("found file {} at {}".format(entry, f))
            return True, f
        else:
            depth += 1
            if depth < DEPTH:
                logger.debug("recursing up one level")
                return _find(
                    os.path.realpath(os.path.join(folder, "..")), entry, folder
                )

            logger.debug("Too many recursive calls")
            return False, ["Too many recursive calls"]

        logger.fatal("SHOULD NOT HAVE EVER GOTTEN HERE!!!")
        exit(42)

    return _find(os.path.realpath(folder), entry)
