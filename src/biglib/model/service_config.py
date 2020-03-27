import io
import json
import logging
import re

import attr

from .service_config_method import ServiceConfigMethod
from .service_config_param import ServiceConfigParam
from .service_config_params import ServiceConfigParams
from .service_config_props import ServiceConfigProps
from .service_config_request_param import ServiceConfigRequestParam
from .service_config_response_param import ServiceConfigResponseParam
from .service_config_version import ServiceConfigVersion

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
        logging.debug(f"load_from_file: {type(file_or_file_path)=}")

        if isinstance(file_or_file_path, io._io.TextIOWrapper):
            logging.debug(
                f"load_from_file: load from open buffered file reader: {file_or_file_path}"
            )
            handle = file_or_file_path

        elif isinstance(file_or_file_path, str):
            logging.debug(
                f"load_from_file: load from string file path: {file_or_file_path}"
            )
            try:
                handle = open(file_or_file_path, "rt")
            except FileNotFoundError as ex:
                err = f"no such file: {file_or_file_path}"
                logging.debug(f"load_from_file: {err}")
                return False, [err]
            except Exception as ex:
                err = f"unexpected exception: {ex}"
                logging.debug(f"load_from_file: {err}")
                return False, [err]

        else:
            err = f"unknown data type = {file_or_file_path}"
            logging.debug(f"load_from_file: {err}")
            return False, [err]

        outcome = False
        # svc_cfg = None

        try:
            logging.debug(f"load_from_file: calling json.load")
            ot = json.load(handle)
            svc_cfg = cls.parse_dict_to_service_config(ot)
            logging.debug(f"load_from_file: [a] {svc_cfg=}")
            outcome = True

        except Exception as ex:
            logging.debug(f"{type(ex)=}")
            svc_cfg = [str(ex)]
            logging.debug(f"load_from_file: [b] {svc_cfg=}")

        logging.debug(f"load_from_file: returning")
        logging.debug(f"load_from_file:     {outcome=}")
        logging.debug(f"load_from_file:     {svc_cfg=}")

        return outcome, svc_cfg

    @classmethod
    def parse_dict_to_service_config(cls, ot) -> ServiceConfig:
        logging.debug(f"parse_dict_to_service_config: {type(ot)=}")

        svc_cfg = ServiceConfig()

        if KEY_VERSION in ot:
            logging.debug(
                f'parse_dict_to_service_config: "{KEY_VERSION}" in ot: "{ot[KEY_VERSION]}"'
            )
            svc_cfg.service_config_version.version = ot[KEY_VERSION]["value"]

        if KEY_METHOD in ot:
            logging.debug(
                f'parse_dict_to_service_config: "{KEY_METHOD}" in ot: "{ot[KEY_METHOD]}"'
            )
            svc_cfg.service_config_method.method = ot[KEY_METHOD]["name"]

        if KEY_REQUESTPARAMS in ot:
            logging.debug(
                f'parse_dict_to_service_config: "{KEY_REQUESTPARAMS}" in ot: "{ot[KEY_REQUESTPARAMS]}"'
            )
            svc_cfg.service_config_request_params = ServiceConfigParams.build(
                ot[KEY_REQUESTPARAMS], ServiceConfigRequestParam
            )

        if KEY_RESPONSEPARAMS in ot:
            logging.debug(
                f'parse_dict_to_service_config: "{KEY_RESPONSEPARAMS}" in ot: "{ot[KEY_RESPONSEPARAMS]}"'
            )
            svc_cfg.service_config_response_params = ServiceConfigParams.build(
                ot[KEY_RESPONSEPARAMS], ServiceConfigResponseParam
            )

        #     #
        #     # for subtree in ot["requestparams"].items():
        #     #     logging.debug(f"{type(subtree)=} :: {subtree=}")
        #     #     # param = build_param(ServiceConfigRequestParam, subtree)
        #     #     param = ServiceConfigRequestParam.build(subtree)
        #     #     logging.debug(f"{type(param)=} {param=}")
        #     #     svc_cfg.service_config_request_params.put(param)
        #
        # if "responseparams" in ot:
        #     for subtree in ot["responseparams"].items():
        #         logging.debug(f"{type(subtree)=} :: {subtree=}")
        #         # param = build_param(ServiceConfigResponseParam, subtree)
        #         param = ServiceConfigResponseParam.build(subtree)
        #         logging.debug(f"{type(param)=} {param=}")
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
