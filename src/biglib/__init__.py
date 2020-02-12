import logging
import os

level = os.getenv("LEVEL", None)
if not level:
    debug = os.getenv("DEBUG", None)
    if debug and debug.upper() == "Y":
        level = "DEBUG"
if level == "DEBUG":
    log_level = logging.DEBUG
elif level == "INFO":
    log_level = logging.INFO
elif level == "WARNING":
    log_level = logging.WARNING
else:
    log_level = logging.INFO
logging.basicConfig(format="%(asctime)s %(levelname)s : %(message)s", level=log_level)
