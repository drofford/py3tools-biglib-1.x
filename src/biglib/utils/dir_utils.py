import errno
import logging
import os

import os.path


def mkdir_p(path):
    try:
        os.makedirs(path)
        logging.debug(f"Created directory: {path}")
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
