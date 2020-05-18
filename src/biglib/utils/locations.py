import errno
import json
# import logging
import os
import os.path
import pprint
import re

from biglib import logger
from memoize import memoize, memoize_with


class Locations:

    props_cache = dict()
    file_path_cache = dict()

    @classmethod
    def get_a_root_dir(cls, proj_name, prop_name):
        logger.debug(f"get_a_root_dir was invoked: {proj_name=} {prop_name=}")
        r, t = cls._read_props_from_file(
            os.path.join(os.getenv("HOME"), ".gradle", "gradle.properties")
        )
        if not r:
            return r, t

        root_dir = t.get(prop_name)
        if not root_dir:
            return False, ["Could not determine the {} root dir".format(proj_name)]

        return True, root_dir

    @classmethod
    @memoize
    def get_interceptas_root_dir(cls):
        logger.debug("get_interceptas_root_dir was invoked")
        return cls.get_a_root_dir("Interceptas", "interceptasHome")

    @classmethod
    @memoize
    def get_vertigo_root_dir(cls):
        logger.debug("get_vertigo_root_dir was invoked")
        return cls.get_a_root_dir("Vertigo", "vertigoHome")

    @classmethod
    def get_path_for_a_vertigo_file(cls, file_subpath):
        logger.debug(f"get_path_for_a_vertigo_file was invoked: {file_subpath=}")

        if file_subpath in cls.file_path_cache:
            logger.debug(
                f"get_path_for_a_vertigo_file: file path FOUND in cache: {file_subpath}"
            )
            t = cls.file_path_cache[file_subpath]

        else:
            logger.debug(
                f"get_path_for_a_vertigo_file: file path NOT FOUND in cache: {file_subpath}"
            )

            r, t = cls.get_vertigo_root_dir()
            if r:
                file_path = os.path.join(t, file_subpath)
                logger.debug("file_subpath = {}".format(file_subpath))
                logger.debug("file_path    = {}".format(file_path))
                if os.path.isfile(file_path):
                    logger.debug(
                        f"get_path_for_a_vertigo_file: file path {file_subpath} was computed and stored in cache"
                    )
                    cls.file_path_cache[file_subpath] = file_path
                    t = file_path
                else:
                    r = False
                    t = ["Could not locate the file: {}".format(file_subpath)]

        return r, t

    @classmethod
    @memoize
    def get_application_properties_path(cls):
        logger.debug("get_application_properties_path was invoked")
        return cls.get_path_for_a_vertigo_file(
            os.path.join("src", "resources", "application.properties")
        )

    @classmethod
    @memoize
    def get_master_properties_path(cls):
        logger.debug("get_master_properties_path was invoked")
        return cls.get_path_for_a_vertigo_file(
            os.path.join("src", "resources", "master.properties")
        )

    @classmethod
    @memoize
    def get_service_definitions_path(cls):
        logger.debug("get_service_definitions_path was invoked")
        return cls.get_path_for_a_vertigo_file(
            os.path.join("src", "resources", "serviceDefinitions.xml")
        )

    @classmethod
    def _read_props_from_file(cls, cfg_file):
        logger.debug(f"_read_props_from_file was invoked: {cfg_file=}")

        if not os.path.isfile(cfg_file):
            return False, "No such file: {}".format(cfg_file)

        cfg = None
        if cfg_file in cls.props_cache:
            logger.debug(f"_read_props_from_file: path FOUND in cache: {cfg_file}")
            cfg = cls.props_cache[cfg_file]

        else:
            logger.debug(f"_read_props_from_file: path NOT FOUND in cache: {cfg_file}")
            cfg = dict()

            with open(cfg_file, "r") as fp:
                for line in fp.readlines():
                    line = line.strip()
                    if len(line) == 0 or line.startswith("#"):
                        continue
                    hits = re.findall("^([^=]+)=(.*)", line)
                    if len(hits) == 1:
                        if len(hits[0]) == 2:
                            k = hits[0][0].strip()
                            v = hits[0][1].strip()
                            if k in cfg:
                                return (False, "Duplicate key: {}".format(k))
                            cfg[k] = v

            logger.debug(
                f"_read_props_from_file: file {cfg_file=} was read in, parsed, and stored in cache"
            )
            cls.props_cache[cfg_file] = cfg

        return True, cfg
