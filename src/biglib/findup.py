import argparse
import logging
import os
import os.path
import sys

DEPTH = 100
depth = 0


def findup(folder, entry):
    def _find(folder, entry, previous=None):
        global depth
        logging.debug("Testing: dir={} for file={}".format(folder, entry))
        logging.debug("    prev dir={}".format(previous))
        if folder == previous:
            logging.debug(
                "Reached top of file system - file not found: {}".format(entry)
            )
            return False, ['Not found: "%s"' % entry]

        f = os.path.realpath(os.path.join(folder, entry))
        logging.debug("testing {}".format(f))
        if os.path.exists(entry) or os.path.isfile(f) or os.path.isdir(f):
            logging.debug("found file {} at {}".format(entry, f))
            return True, f
        else:
            depth += 1
            if depth < DEPTH:
                logging.debug("recursing up one level")
                return _find(
                    os.path.realpath(os.path.join(folder, "..")), entry, folder
                )

            logging.debug("Too many recursive calls")
            return False, ["Too many recursive calls"]

        logging.fatal("SHOULD NOT HAVE EVER GOTTEN HERE!!!")
        exit(42)

    return _find(os.path.realpath(folder), entry)
