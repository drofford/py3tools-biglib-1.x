# import logging
import os
import os.path
import re

import py.test
from biglib import logger
from biglib.model.service_config_props import ServiceConfigProps


def test_empty() -> None:
    m = ServiceConfigProps()
    assert len(m) == 0
    assert len(m.prop_names()) == 0


def test_put_and_get() -> None:
    m = ServiceConfigProps()

    m.put("organization", "Krusty Krab")
    assert len(m) == 1
    assert len(m.prop_names()) == 1

    names = m.prop_names()
    assert isinstance(names, list)
    assert len(names) == 1
    assert m.prop_names() == ["organization"]

    assert m.get("organization") == (True, "Krusty Krab")
    assert m["organisation"] == (False, ["Property not found: organisation"])

    m.put("favorite", "Squidward")
    m.put("number_of_employees", "3")

    assert len(m) == 3
    assert len(m.prop_names()) == 3
    assert m.prop_names() == ["favorite", "number_of_employees", "organization"]
