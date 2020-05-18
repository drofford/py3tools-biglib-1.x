# import logging as log
import os.path
import re

from ..model.properties import Properties


class PropertiesHelper(object):
    def __init__(self):
        return

    @classmethod
    def load_from_file(cls, props_file_path):
        f = os.path.realpath(os.path.join(os.getcwd(), props_file_path))
        logger.debug(
            """{cl}#{fu} : props_file_path='{pf}'.""".format(
                cl="PropertiesHelper",
                fu="load_properties_from_file",
                pf=props_file_path,
            )
        )
        logger.debug(
            """{cl}#{fu} : current dir    ='{cd}'.""".format(
                cl="PropertiesHelper", fu="load_properties_from_file", cd=os.getcwd()
            )
        )
        logger.debug(
            """{cl}#{fu} : full    path   ='{fd}'.""".format(
                cl="PropertiesHelper", fu="load_properties_from_file", fd=f
            )
        )
        if not os.path.exists(props_file_path):
            return False, ["""No such file: '{}'.""".format(props_file_path)]

        if not os.path.isfile(props_file_path):
            return False, ["""Not a file: '{}'.""".format(props_file_path)]

        return cls.load_from_open_file(open(props_file_path, "r"))

    @classmethod
    def load_from_open_file(cls, file_handle):
        logger.debug(
            """{cl}#{fu}.""".format(
                cl="PropertiesHelper", fu="load_properties_from_openfile"
            )
        )

        props = Properties()

        try:
            for line in file_handle:
                line = line.strip()
                if len(line) == 0 or line[0] == "#":
                    continue

                h = re.findall("([^=]+)=(.+)", line)
                if len(h) == 0 or len(h[0]) != 2:
                    continue
                logger.debug("""read property file line '{}'.""".format(line))

                props.put(h[0][0], h[0][1])

        except Exception as ex:
            return (
                False,
                [
                    """Exception {} occurred while processing properties file '{}'.""".format(
                        ex, str(file_handle)
                    )
                ],
            )

        return True, props
