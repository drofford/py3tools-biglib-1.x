import importlib
import logging
import os
import pkgutil
import sys

from pkgutil import ModuleInfo


def find_modules(start_mod_name: str, when=None, do=None) -> bool:
    logging.debug(f'find_mods.py :: find_modules :: {start_mod_name=}')

    def dummy_when(mod_full_name: str, mod_info: ModuleInfo) -> bool:
        return True

    def dummy_do(mod_full_name: str, mod_info: ModuleInfo, sub_mod_data: object) -> None:
        pass

    _when = dummy_when if when is None else when
    _do   = dummy_do   if do   is None else do

    def search(mod_name: str, level: int) -> None:
        ind = "    " * level
        logging.debug(f"{ind}sparky :: find_mods.py :: search({mod_name})")

        if level > 8:
            logging.error(f"level reached {level}")
            exit(0)

        mod_data = importlib.import_module(mod_name)
        logging.debug(f"{ind}module = {mod_data}")

        for mod_info in pkgutil.iter_modules(mod_data.__path__):
            logging.debug(f"{ind}  submod name = {mod_info.name}, ispkg = {mod_info.ispkg}")
            full_mod_name = f"{mod_name}.{mod_info.name}"
            if mod_info.ispkg:
                # logging.debug(f"search(\"{full_mod_name}\", {level+1})")
                search(full_mod_name, level + 1)
            # elif mod_info.name.startswith("check_"):
            elif _when(full_mod_name, mod_info):
                sub_mod_data = importlib.import_module(full_mod_name)
                logging.debug(f"Found sub module: {full_mod_name}")
                logging.debug(f"{mod_info=}")
                logging.debug(f"{sub_mod_data=}")
                _do(full_mod_name, mod_info, sub_mod_data)
            else:
                logging.debug(f"Ignoring module: {mod_name}.{mod_info.name}")

    search(start_mod_name, 0)
    return True
