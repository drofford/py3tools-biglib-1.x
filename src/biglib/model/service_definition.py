import attr


@attr.s
class ServiceDefinition:
    service_name = attr.ib(default=None)
    service_nice_name = attr.ib(default=None)
    service_instance_class_name = attr.ib(default=None)
    service_worker_instance_class_name = attr.ib(default=None)
    is_sharded = attr.ib(default=None)
    is_write_behind = attr.ib(default=None)
    write_behind_service = attr.ib(default=None)
    service_write_behind_filter_class = attr.ib(default=None)
    monitor_performance = attr.ib(default=None)
    is_external_service = attr.ib(default=None)

    def copy_from(self, source) -> None:
        if source is None:
            raise TypeError(f"cannot copy data from None")
        if not isinstance(source, ServiceDefinition):
            raise TypeError(
                f"trying to copy data from an object that is not a ServiceDefinition: {type(source)}"
            )

        self.service_name = source.service_name
        self.service_nice_name = source.service_nice_name
        self.service_instance_class_name = source.service_instance_class_name
        self.service_worker_instance_class_name = (
            source.service_worker_instance_class_name
        )
        self.is_sharded = source.is_sharded
        self.is_write_behind = source.is_write_behind
        self.write_behind_service = source.write_behind_service
        self.service_write_behind_filter_class = (
            source.service_write_behind_filter_class
        )
        self.monitor_performance = source.monitor_performance
        self.is_external_service = source.is_external_service
