import attr

from .service_config_param import ServiceConfigParam


@attr.s
class ServiceConfigResponseParam(ServiceConfigParam):
    param_path = attr.ib(default="")

    @classmethod
    def build(cls, subtree):
        if not isinstance(subtree, tuple):
            raise ValueError(
                f"{cls.__name__}#build: subtree of type {type(subtree)} is invalid"
            )
        if len(subtree) != 2:
            raise ValueError(
                f"{cls.__name__}#build: subtree tuple of size {len(subtree)} is invalid"
            )
        if not isinstance(subtree[0], str):
            raise ValueError(
                f"{cls.__name__}#build: subtree tuple element 0 of type {type(subtree[0])} is invalid"
            )
        if not isinstance(subtree[1], dict):
            raise ValueError(
                f"{cls.__name__}#build: subtree tuple element 1 of type {type(subtree[1])} is invalid"
            )

        pn = subtree[0]
        pi = subtree[1].get("id")
        pt = subtree[1].get("type")
        pf = subtree[1].get("format")

        param = ServiceConfigResponseParam(
            param_name=pn, param_path=pi, param_type=pt, param_format=pf,
        )

        return param
