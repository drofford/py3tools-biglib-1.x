# import logging

import attr
from biglib import logger

from .service_config_param import ServiceConfigParam


@attr.s
class ServiceConfigParams:
    params = attr.ib(default=attr.Factory(dict))

    @classmethod
    def build(cls, subtree, param_class):
        logger.debug(f"ServiceConfigParams##build: {'-'*80}")
        logger.debug(f"ServiceConfigParams##build: {type(subtree)=}")
        logger.debug(f"ServiceConfigParams##build: {subtree=}")
        logger.debug(f"ServiceConfigParams##build: {param_class=}")

        params = ServiceConfigParams()

        for item in subtree.items():
            logger.debug(f"ServiceConfigParams##build: {type(item)=} :: {item=}")
            param = param_class.build(item)
            logger.debug(f"ServiceConfigParams##build: {type(param)=} {param=}")
            params.put(param)

        logger.debug(f"ServiceConfigParams##build: {'-'*80}")
        return params

    def __len__(self) -> int:
        return len(self.params)

    def get(self, name: str) -> [bool, ServiceConfigParam]:

        if name not in self.params:
            return False, [f"No param with the name {name}"]
        return True, self.params[name]

    def put(self, param: ServiceConfigParam) -> [bool, object]:
        if param.param_name in self.params:
            return False, [f"Duplicate param name: {param.param_name}"]
        self.params[param.param_name] = param
        return True, None
