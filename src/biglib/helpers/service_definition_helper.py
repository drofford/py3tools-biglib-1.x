import logging as log
import os
import os.path
import re
import sys
# import xmltodict
import xml.etree.ElementTree as ET

from ..model.service_definition import ServiceDefinition
from ..model.service_definitions import ServiceDefinitions


class ServiceDefinitionHelper:
    @classmethod
    def load_from_file(cls, file_name):
        if not os.path.isfile(file_name):
            return False, ["No such file: {}".format(file_name)]
        root = ET.parse(file_name)
        log.debug("Read XML from {} into {}".format(file_name, root))

        log.debug("Getting all external service names")
        service_names = cls.get_all_ext_service_names(root)
        log.debug(
            "Retrieved {} external service names: {}".format(
                len(service_names), service_names
            )
        )

        service_defs = ServiceDefinitions()

        for service_name in service_names:
            log.debug("=" * 100)
            log.debug(
                "Retrieving service definition for service name {}".format(service_name)
            )
            r, service_def = cls.get_ext_service_by_name(root, service_name)
            if r:
                log.debug("Retrieved {}".format(service_def))
                service_defs.put(service_name, service_def)
        log.debug("=" * 100)

        return True, service_defs

    @classmethod
    def get_all_ext_service_names(cls, root):
        def filter(service):
            return True
            # return "external.vendor" in cls._field_finder(
            #     service, "serviceWorkerClassName"
            # )

        return cls._get_filtered_names(root, filter)

    @classmethod
    def get_ext_service_by_name(cls, root, service_name):
        service_definition = None
        for service in root.findall("service"):
            if service.find("name").text == service_name:
                service_def = service_definition = ServiceDefinition(service_name)

                service_def.service_nice_name = cls._field_finder(service, "niceName")
                service_def.service_instance_class_name = cls._field_finder(
                    service, "serviceClassName"
                )
                service_def.service_worker_instance_class_name = cls._field_finder(
                    service, "serviceWorkerClassName"
                )
                service_def.is_sharded = cls._field_finder(service, "isSharded")
                service_def.is_write_behind = cls._field_finder(
                    service, "isWriteBehind"
                )
                service_def.write_behind_service = cls._field_finder(
                    service, "writeBehindService"
                )
                service_def.service_write_behind_filter_class = cls._field_finder(
                    service, "serviceWriteBehindFilterClassName"
                )
                service_def.monitor_performance = cls._field_finder(
                    service, "monitorPerformance"
                )
                service_def.is_external_service = (
                    "external.vendor" in service_def.service_worker_instance_class_name
                )

                return True, service_definition
        return (
            False,
            ["No service definition found for service {}".format(service_name)],
        )

    @classmethod
    def _get_filtered_names(cls, root, filter=None):
        svcs = [
            service.find("name").text
            for service in root.findall("service")
            if filter is None or filter(service)
        ]
        log.debug("Found services: {}".format(svcs))
        return svcs

    @classmethod
    def _field_finder(cls, service, field):
        try:
            svc = service.find(field).text
            log.debug("Found service: {}".format(svc))
            return svc
        except AttributeError:
            return None
