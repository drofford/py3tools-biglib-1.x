from biglib.model.service_config_response_param import \
    ServiceConfigResponseParam


def test_create_empty() -> None:
    param = ServiceConfigResponseParam()
    assert param.param_name == ""
    assert param.param_path == ""
    assert param.param_type == ""
    assert param.param_format == ""


def test_create_with_positionals1() -> None:
    param = ServiceConfigResponseParam("First Name", "text", "format", "$.name.first")
    assert param.param_name == "First Name"
    assert param.param_path == "$.name.first"
    assert param.param_type == "text"
    assert param.param_format == "format"


def test_create_with_names1() -> None:
    param = ServiceConfigResponseParam(
        param_name="First Name",
        param_path="//name/first",
        param_type="text",
        param_format="format",
    )
    assert param.param_name == "First Name"
    assert param.param_path == "//name/first"
    assert param.param_type == "text"
    assert param.param_format == "format"


def test_create_from_builder() -> None:
    subtree = (
        "First Name",
        {"id": "//name/first", "type": "text", "format": "application/text",},
    )

    param = ServiceConfigResponseParam.build(subtree)
    assert param is not None
    assert isinstance(param, ServiceConfigResponseParam)
    assert param.param_name == "First Name"
    assert param.param_path == "//name/first"
    assert param.param_type == "text"
    assert param.param_format == "application/text"
