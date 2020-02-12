import attr
import io
import json
import logging
import re

from .service_config_version import ServiceConfigVersion
from .service_config_method import ServiceConfigMethod
from .service_config_param import ServiceConfigParam
from .service_config_params import ServiceConfigParams
from .service_config_props import ServiceConfigProps
from .service_config_request_param import ServiceConfigRequestParam
from .service_config_response_param import ServiceConfigResponseParam

KEY_METHOD = "method"
KEY_REQUESTPARAMS = "requestparams"
KEY_RESPONSEPARAMS = "responseparams"
KEY_VERSION = "version"

class ServiceConfig:
    ...

@attr.s
class ServiceConfig:

    service_config_version = attr.ib(default=attr.Factory(ServiceConfigVersion))
    service_config_method = attr.ib(default=attr.Factory(ServiceConfigMethod))
    service_config_props = attr.ib(default=attr.Factory(ServiceConfigProps))
    service_config_request_params = attr.ib(default=attr.Factory(ServiceConfigParams))
    service_config_response_params = attr.ib(default=attr.Factory(ServiceConfigParams))

    @classmethod
    def load_from_file(cls, file_or_file_path):
        logging.debug(f"{type(file_or_file_path)=}")

        if isinstance(file_or_file_path, io._io.TextIOWrapper):
            logging.debug(f"load from open buffered file reader: {file_or_file_path}")
            handle = file_or_file_path

        elif isinstance(file_or_file_path, str):
            logging.debug(f"load from string file path: {file_or_file_path}")
            try:
                handle = open(file_or_file_path, "rt")
            except FileNotFoundError as ex:
                err = f"no such file: {file_or_file_path}"
                logging.debug(err)
                return False, [err]
            except Exception as ex:
                err = f"unexpected exception: {ex}"
                logging.debug(err)
                return False, [err]

        else:
            return False, [f"unknown data type = {file_or_file_path}"]

        outcome = False
        # svc_cfg = None

        try:
            ot = json.load(handle)
            svc_cfg = cls.parse_dict_to_service_config(ot)
            logging.info(f"[a] {svc_cfg=}")
            outcome = True

        except Exception as ex:
            logging.error(f"{type(ex)=}")
            svc_cfg = [str(ex)]
            logging.info(f"[b] {svc_cfg=}")

        return outcome, svc_cfg

    @classmethod
    def parse_dict_to_service_config(cls, ot) -> ServiceConfig:

        svc_cfg = ServiceConfig()

        if KEY_VERSION in ot:
            svc_cfg.service_config_version.version = ot[KEY_VERSION]["value"]

        if KEY_METHOD in ot:
            svc_cfg.service_config_method.method = ot[KEY_METHOD]["name"]

        if KEY_REQUESTPARAMS in ot:
            svc_cfg.service_config_request_params = ServiceConfigParams.build(
                ot[KEY_REQUESTPARAMS], ServiceConfigRequestParam
            )
        if KEY_RESPONSEPARAMS in ot:
            svc_cfg.service_config_response_params = ServiceConfigParams.build(
                ot[KEY_RESPONSEPARAMS], ServiceConfigResponseParam
            )

        #     #
        #     # for subtree in ot["requestparams"].items():
        #     #     logging.info(f"{type(subtree)=} :: {subtree=}")
        #     #     # param = build_param(ServiceConfigRequestParam, subtree)
        #     #     param = ServiceConfigRequestParam.build(subtree)
        #     #     logging.info(f"{type(param)=} {param=}")
        #     #     svc_cfg.service_config_request_params.put(param)
        #
        # if "responseparams" in ot:
        #     for subtree in ot["responseparams"].items():
        #         logging.info(f"{type(subtree)=} :: {subtree=}")
        #         # param = build_param(ServiceConfigResponseParam, subtree)
        #         param = ServiceConfigResponseParam.build(subtree)
        #         logging.info(f"{type(param)=} {param=}")
        #         svc_cfg.service_config_response_params.put(param)
        #
        return svc_cfg

    def get_service_config_version(self) -> [bool, str]:
        x = self.service_config_version.version
        return True, x.strip() if x is not None else ""

    def get_service_config_method(self) -> [bool, str]:
        x = self.service_config_method.method
        return True, x.strip() if x is not None else ""

    def get_service_request_params(self) -> ServiceConfigParams:
        x = self.service_config_request_params
        return True, x

    def get_service_response_params(self) -> ServiceConfigParams:
        x = self.service_config_response_params
        return x
