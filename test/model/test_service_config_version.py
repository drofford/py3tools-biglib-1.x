from biglib.model.service_config_version import ServiceConfigVersion


def test_create_empty() -> None:
    service_config_version = ServiceConfigVersion()
    assert service_config_version.version == ""


def test_create_with_positionals() -> None:
    service_config_version = ServiceConfigVersion("1.x")
    assert service_config_version.version == "1.x"


def test_create_with_names() -> None:
    service_config_version = ServiceConfigVersion(version="2.y")
    assert service_config_version.version == "2.y"
