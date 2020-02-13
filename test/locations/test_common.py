import logging
import os
import os.path
import re
import sys

os.putenv("HOME", "/Users/gofford")
logging.warning(f"set env var HOME to {os.getenv('HOME')}")

from biglib.locations.common import find_home_dir


def test_find_home_dir():
    logging.warning(f"test_find_home_dir: entry")
    r, hd = find_home_dir()
    logging.warning(f"test_find_home_dir: {r=}")
    logging.warning(f"test_find_home_dir: {hd=}")

    assert r
    assert os.getenv("HOME") == hd
