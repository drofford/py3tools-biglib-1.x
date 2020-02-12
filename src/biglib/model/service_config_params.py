import attr
import logging

from .service_config_param import ServiceConfigParam


@attr.s
class ServiceConfigParams:
    params = attr.ib(default=attr.Factory(dict))

    @classmethod
    def build(cls, subtree, param_class):
        logging.info(f"{type(subtree)=} :: {subtree=} :: {param_class=}")
        params = ServiceConfigParams()

        for item in subtree.items():
            logging.info(f"{type(item)=} :: {item=}")
            param = param_class.build(item)
            logging.info(f"{type(param)=} {param=}")
            params.put(param)

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
