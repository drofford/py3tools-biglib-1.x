import errno
# import logging
import os
import os.path

from biglib import logger


def mkdir_p(path):
    try:
        os.makedirs(path)
        logger.debug(f"Created directory: {path}")
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
