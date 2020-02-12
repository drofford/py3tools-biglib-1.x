import attr


@attr.s
class ServiceConfigParam:
    param_name = attr.ib(default="")
    param_type = attr.ib(default="")
    param_format = attr.ib(default="")
