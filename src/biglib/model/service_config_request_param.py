import logging

import attr

from .service_config_param import ServiceConfigParam


@attr.s
class ServiceConfigRequestParam(ServiceConfigParam):
    param_id = attr.ib(default="")
    param_required = attr.ib(default=False)

    @classmethod
    def build(cls, subtree):
        logging.debug(f"ServiceConfigRequestParam##build: {subtree=}")

        if not isinstance(subtree, tuple):
            err = f"{cls.__name__}#build: subtree of type {type(subtree)} is invalid"
            logging.debug(f"ServiceConfigRequestParam##build: {err}")
            raise ValueError(err)

        if len(subtree) != 2:
            err = (
                f"{cls.__name__}#build: subtree tuple of size {len(subtree)} is invalid"
            )
            logging.debug(f"ServiceConfigRequestParam##build: {err}")
            raise ValueError(err)

        if not isinstance(subtree[0], str):
            err = f"{cls.__name__}#build: subtree tuple element 0 of type {type(subtree[0])} is invalid"
            logging.debug(f"ServiceConfigRequestParam##build: {err}")
            raise ValueError(err)

        if not isinstance(subtree[1], dict):
            raise ValueError(
                f"{cls.__name__}#build: subtree tuple element 1 of type {type(subtree[1])} is invalid"
            )
            logging.debug(f"ServiceConfigRequestParam##build: {err}")
            raise ValueError(err)

        pn = subtree[0]
        pi = subtree[1].get("id")
        pt = subtree[1].get("type")
        pf = subtree[1].get("format")
        pr = subtree[1].get("required")
        logging.debug(f"ServiceConfigRequestParam##build: {pn=}")
        logging.debug(f"ServiceConfigRequestParam##build: {pi=}")
        logging.debug(f"ServiceConfigRequestParam##build: {pt=}")
        logging.debug(f"ServiceConfigRequestParam##build: {pf=}")
        logging.debug(f"ServiceConfigRequestParam##build: {pr=}")

        param = ServiceConfigRequestParam(
            param_name=pn,
            param_id=pi,
            param_type=pt,
            param_format=pf,
            param_required=pr,
        )
        logging.debug(f"ServiceConfigRequestParam##build: {param=}")

        return param
