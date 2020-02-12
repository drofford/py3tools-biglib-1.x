import attr


@attr.s
class ServiceConfigMethod:
    method = attr.ib(default="")
