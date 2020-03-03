from biglib.model.service_config_request_param import ServiceConfigRequestParam


def test_create_empty() -> None:
    param = ServiceConfigRequestParam()
    assert param.param_name == ""
    assert param.param_id == ""
    assert param.param_type == ""
    assert param.param_format == ""


def test_create_with_positionals1() -> None:
    param = ServiceConfigRequestParam("First Name", "text", "format", "first_name")
    assert param.param_name == "First Name"
    assert param.param_id == "first_name"
    assert param.param_type == "text"
    assert param.param_format == "format"
    assert not param.param_required


def test_create_with_positionals2() -> None:
    param = ServiceConfigRequestParam(
        "First Name", "text", "format", "first_name", True
    )
    assert param.param_name == "First Name"
    assert param.param_id == "first_name"
    assert param.param_type == "text"
    assert param.param_format == "format"
    assert param.param_required


def test_create_with_names1() -> None:
    param = ServiceConfigRequestParam(
        param_name="First Name",
        param_id="first_name",
        param_type="text",
        param_format="format",
    )
    assert param.param_name == "First Name"
    assert param.param_id == "first_name"
    assert param.param_type == "text"
    assert param.param_format == "format"
    assert not param.param_required


def test_create_with_names2() -> None:
    param = ServiceConfigRequestParam(
        param_name="First Name",
        param_id="first_name",
        param_type="text",
        param_format="format",
        param_required=True,
    )
    assert param.param_name == "First Name"
    assert param.param_id == "first_name"
    assert param.param_type == "text"
    assert param.param_format == "format"
    assert param.param_required


def test_create_from_builder() -> None:
    subtree = (
        "First Name",
        {
            "id": "first_name",
            "type": "text",
            "format": "application/text",
            "required": True,
        },
    )

    param = ServiceConfigRequestParam.build(subtree)
    assert param is not None
    assert isinstance(param, ServiceConfigRequestParam)
    assert param.param_name == "First Name"
    assert param.param_id == "first_name"
    assert param.param_type == "text"
    assert param.param_format == "application/text"
    assert param.param_required
