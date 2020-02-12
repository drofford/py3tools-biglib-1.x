import attr

from .model.service_definition import ServiceDefinition


@attr.s
class ExtendedServiceDefinition(ServiceDefinition):
    def _converter(value):
        if value is None:
            value = set()
        elif isinstance(value, set):
            pass
        elif isinstance(value, str):
            value = set([value])
        else:
            value = set(value)
        return value

    namespaces = attr.ib(default=None, converter=_converter)
    methods = attr.ib(default=None, converter=_converter)
    versions = attr.ib(default=None, converter=_converter)
    base_urls = attr.ib(default=None, converter=_converter)
