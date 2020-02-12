from biglib.model.service_definition import ServiceDefinition


def _create_kiki(tweak="") -> ServiceDefinition:
    sd = ServiceDefinition(
        service_name=f"kiki{tweak}",
        service_nice_name=f"kiki's delivery service{tweak}",
        service_instance_class_name=f"com.service.delivery.kiki.KikiDeliverServiceInstance{tweak}",
        service_worker_instance_class_name=f"com.service.delivery.kiki.KikiDeliverServiceWorkerInstance{tweak}",
    )
    return sd
