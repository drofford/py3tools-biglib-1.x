from biglib.model.service_config_method import ServiceConfigMethod


def test_create_empty() -> None:
    service_config_method = ServiceConfigMethod()
    assert service_config_method.method == ""


def test_create_with_positionals() -> None:
    service_config_method = ServiceConfigMethod("READ")
    assert service_config_method.method == "READ"


def test_create_with_names() -> None:
    service_config_method = ServiceConfigMethod(method="WRITE")
    assert service_config_method.method == "WRITE"
