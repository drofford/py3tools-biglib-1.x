from biglib.model.service_config_param import ServiceConfigParam


def test_create_empty() -> None:
    param = ServiceConfigParam()
    assert param.param_name == ""
    assert param.param_type == ""
    assert param.param_format == ""


def test_create_with_ctor_only() -> None:
    param = ServiceConfigParam("First Name", "text", "format")
    assert param.param_name == "First Name"
    assert param.param_type == "text"
    assert param.param_format == "format"
