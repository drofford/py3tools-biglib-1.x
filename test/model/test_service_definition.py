import logging
import re
from test.model.helpers import _create_kiki

import py.test
from biglib.model.service_definition import ServiceDefinition


def test_create_empty() -> None:
    logging.debug("test_create_empty")
    sd = ServiceDefinition()
    assert sd is not None
    assert sd.service_name is None
    assert sd.service_nice_name is None
    assert sd.service_instance_class_name is None
    assert sd.service_worker_instance_class_name is None
    assert sd.is_sharded is None
    assert sd.is_write_behind is None
    assert sd.write_behind_service is None
    assert sd.service_write_behind_filter_class is None
    assert sd.monitor_performance is None
    assert sd.is_external_service is None


def test_create_valid_svc_def() -> None:
    sd = _create_kiki()
    assert sd is not None
    assert sd.service_name == "kiki"
    assert sd.service_nice_name == "kiki's delivery service"
    assert (
        sd.service_instance_class_name
        == "com.service.delivery.kiki.KikiDeliverServiceInstance"
    )
    assert (
        sd.service_worker_instance_class_name
        == "com.service.delivery.kiki.KikiDeliverServiceWorkerInstance"
    )
    assert sd.is_sharded is None
    assert sd.is_write_behind is None
    assert sd.write_behind_service is None
    assert sd.service_write_behind_filter_class is None
    assert sd.monitor_performance is None
    assert sd.is_external_service is None


def test_copy_from_valid_svc_def() -> None:
    src = _create_kiki()
    assert src is not None
    assert src.service_name == "kiki"
    assert src.service_nice_name == "kiki's delivery service"
    assert (
        src.service_instance_class_name
        == "com.service.delivery.kiki.KikiDeliverServiceInstance"
    )
    assert (
        src.service_worker_instance_class_name
        == "com.service.delivery.kiki.KikiDeliverServiceWorkerInstance"
    )
    assert src.is_sharded is None
    assert src.is_write_behind is None
    assert src.write_behind_service is None
    assert src.service_write_behind_filter_class is None
    assert src.monitor_performance is None
    assert src.is_external_service is None

    dst = ServiceDefinition()
    assert dst is not None
    assert dst.service_name is None
    assert dst.service_nice_name is None
    assert dst.service_instance_class_name is None
    assert dst.service_worker_instance_class_name is None
    assert dst.is_sharded is None
    assert dst.is_write_behind is None
    assert dst.write_behind_service is None
    assert dst.service_write_behind_filter_class is None
    assert dst.monitor_performance is None
    assert dst.is_external_service is None

    dst.copy_from(src)
    assert dst.service_name == "kiki"
    assert dst.service_nice_name == "kiki's delivery service"
    assert (
        dst.service_instance_class_name
        == "com.service.delivery.kiki.KikiDeliverServiceInstance"
    )
    assert (
        dst.service_worker_instance_class_name
        == "com.service.delivery.kiki.KikiDeliverServiceWorkerInstance"
    )
    assert dst.is_sharded is None
    assert dst.is_write_behind is None
    assert dst.write_behind_service is None
    assert dst.service_write_behind_filter_class is None
    assert dst.monitor_performance is None
    assert dst.is_external_service is None
