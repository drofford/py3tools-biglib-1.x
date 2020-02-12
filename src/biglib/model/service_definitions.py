import logging
import io
import re
import xml.etree.ElementTree as ET

from fuzzywuzzy import fuzz, process

# from singleton_decorator import singleton

from .service_definition import ServiceDefinition


# @singleton
class ServiceDefinitions:
    @classmethod
    def load_from_file(cls, file_or_file_path):
        def get_text(xml_subtree, name):
            node = xml_subtree.find(name)
            if node is None:
                return ""
            return node.text

        logging.debug(f"{type(file_or_file_path)=}")
        if isinstance(file_or_file_path, io._io.TextIOWrapper):
            logging.debug(f"load from open buffered file reader: {file_or_file_path}")
            handle = file_or_file_path
        elif isinstance(file_or_file_path, str):
            logging.debug(f"load from string file path: {file_or_file_path}")
            handle = open(file_or_file_path, "rt")
        else:
            return False, [f"unknown data type = {file_or_file_path}"]

        # svc_defs = dict()
        svc_defs = ServiceDefinitions()
        root = ET.fromstring("\n".join(handle.readlines()))
        nodes = root.findall(".//service")
        for node in nodes:
            svc_def = ServiceDefinition()
            svc_def.service_name = get_text(node, "name")
            svc_def.service_nice_name = get_text(node, "niceName")
            svc_def.service_instance_class_name = get_text(node, "serviceClassName")
            svc_def.service_worker_instance_class_name = get_text(
                node, "serviceWorkerClassName"
            )
            svc_def.is_sharded = get_text(node, "isSharded")
            svc_def.is_write_behind = get_text(node, "isWriteBehind")
            svc_def.write_behind_service = get_text(node, "writeBehindService")
            svc_def.service_write_behind_filter_class = get_text(
                node, "serviceWarmupClassName"
            )
            svc_def.monitor_performance = get_text(node, "monitorPerformance")
            svc_def.is_external_service = svc_def.service_instance_class_name.startswith(
                "com.accertify.service.external."
            )
            logging.debug(f"loaded {svc_def}")
            svc_defs.put(svc_def.service_name, svc_def)
        logging.debug(
            f"Loaded {len(svc_defs)} external service definition{'' if len(svc_defs) == 1 else 's'} from file {handle.name}"
        )

        return True, svc_defs

    def __init__(self):
        self.table = dict()

    def __len__(self) -> int:
        return len(self.table)

    def __str__(self) -> str:
        return str(self.table)

    def __getitem__(self, name: str) -> [bool, object]:
        try:
            return True, self.table[name]
        except KeyError:
            return False, [f"Not a service: {name}"]

    def __setitem__(self, name: str, value: str) -> None:
        self.table[name] = value

    def get(self, name: str) -> [bool, object]:
        try:
            return True, self.table[name]
        except KeyError:
            return False, [f"Not a service: {name}"]

    def put(self, name, value) -> None:
        self.table[name] = value

    def reset(self) -> None:
        self.table = dict()

    # kwargs:
    #       pattern = regex to select a subset of names
    #
    def service_names(self, /, pattern=None, fuzzy=False) -> set:

        all_names = self.table.keys()

        def extract_using_pattern(pattern) -> set:
            pattern = "^" + pattern + "$"
            logging.debug("=" * 100)
            logging.debug("""Looking for pattern "{}".""".format(pattern))
            some_names = set()
            for name in all_names:
                logging.debug("-" * 100)
                logging.debug(
                    """Testing name "{}" against pattern "{}".""".format(name, pattern)
                )
                h = re.findall(pattern, name)
                logging.debug(
                    """type(h) = {}, len(h) = {}, data(h) = "{}".""".format(
                        type(h), len(h), h
                    )
                )
                if len(h) == 0:
                    logging.debug("no hit")
                    continue
                hit = None
                if type(h[0]) is list:
                    if len(h[0]) > 0:
                        hit = h[0][0]
                else:
                    hit = h[0]
                logging.debug("""hit = "{}".""".format(hit))
                if hit is not None:
                    some_names.add(hit)
            logging.debug("=" * 100)
            return some_names

        def extract_using_fuzzy(term) -> set:
            possibles = process.extract(term, all_names)
            logging.debug("possibles      = {}".format(possibles))
            good_possibles = [g[0] for g in possibles if g[1] > 70]
            logging.debug("good possibles = {}".format(good_possibles))
            return set(good_possibles)

        if pattern:
            if fuzzy:
                return extract_using_fuzzy(pattern)
            return extract_using_pattern(pattern)

        return set(all_names)

    def is_service(self, service_name):
        return service_name in self.table

    def is_external_service(self, service_name):
        return (
            self.is_service(service_name)
            and self.table[service_name].is_external_service
        )
