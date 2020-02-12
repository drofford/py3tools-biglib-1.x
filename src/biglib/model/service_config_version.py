import attr


@attr.s
class ServiceConfigVersion:
    version = attr.ib(default="")
