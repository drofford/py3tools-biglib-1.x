from biglib.model.service_config_request_param import ServiceConfigRequestParam
from biglib.model.service_config_params import ServiceConfigParams


def make_param(name=None) -> ServiceConfigRequestParam:
    return ServiceConfigRequestParam(
        param_name="First Name" if name is None else name,
        param_id="first_name",
        param_type="text",
        param_format="format",
        param_required=True,
    )


def test_create_empty() -> None:
    params = ServiceConfigParams()
    assert len(params) == 0


def test_create_and_add() -> None:
    params = ServiceConfigParams()

    r, t = params.put(make_param())
    assert r
    assert t is None
    assert len(params) == 1


def test_create_and_add_another() -> None:
    params = ServiceConfigParams()

    r, t = params.put(make_param("a"))
    assert r
    assert t is None
    assert len(params) == 1

    r, t = params.put(make_param("b"))
    assert r
    assert t is None

    assert len(params) == 2


def test_create_and_add_again() -> None:
    params = ServiceConfigParams()

    r, t = params.put(make_param())
    assert r
    assert t is None
    assert len(params) == 1

    r, t = params.put(make_param())
    assert not r
    assert isinstance(t, list)
    assert t[0] == "Duplicate param name: First Name"

    assert len(params) == 1


def test_builder_for_request_params() -> None:
    subtree1 = {
        "id": "first_name",
        "type": "text",
        "format": "application/text",
        "required": True,
    }
    subtree2 = {
        "id": "last_name",
        "type": "text",
        "format": "application/text",
        "required": False,
    }
    group1 = {"requestparams": {
        "First Name": subtree1,
        "Last Name": subtree2,
    }}  # TODO remove this if the next line works
    # group1 = [subtree1, subtree2]

    params = ServiceConfigParams.build(group1, ServiceConfigRequestParam)
    assert params is not None
    assert isinstance(params, ServiceConfigParams)
