import logging
import os
import os.path
import py.test
import re

from biglib.model.service_definition import ServiceDefinition
from biglib.model.service_definitions import ServiceDefinitions

from test.model.helpers import _create_kiki

TEST_XML_FILE_1 = os.path.join("test", "data", "xml", "simple1.xml")
TEST_XML_FILE_2 = os.path.join("test", "data", "xml", "simple2.xml")
REAL_XML_FILE = os.path.join(
    "/Users/gofford",
    "projects",
    "vertigo",
    "src",
    "resources",
    "serviceDefinitions.xml",
)


def test_basic() -> None:
    m = ServiceDefinitions()
    m.reset()

    m = ServiceDefinitions()
    assert len(m) == 0

    sd = _create_kiki()
    m.put(sd.service_name, sd)
    assert len(m) == 1


def test_add_two_svc_defs() -> None:
    m = ServiceDefinitions()
    m.reset()
    assert len(m) == 0

    sd = _create_kiki("A")
    m.put(sd.service_name, sd)
    assert len(m) == 1

    sd = _create_kiki("B")
    m.put(sd.service_name, sd)
    assert len(m) == 2


def test_add_two_svc_defs() -> None:
    m = ServiceDefinitions()
    m.reset()
    assert len(m) == 0

    sd = _create_kiki("A")
    m.put(sd.service_name, sd)
    assert len(m) == 1

    sd = _create_kiki("B")
    m.put(sd.service_name, sd)
    assert len(m) == 2


def test_load_from_file() -> None:
    # m = ServiceDefinitions()
    r, svc_defs = ServiceDefinitions.load_from_file(open(TEST_XML_FILE_1, "rt"))
    logging.debug(f"{svc_defs.table=}")
    assert r
    assert svc_defs is not None
    assert isinstance(svc_defs, ServiceDefinitions)
    assert len(svc_defs) == 1
    r, svc_def = svc_defs.get("sparkyidverify")
    assert r
    logging.debug(f"{svc_def=}")

    assert svc_def is not None
    assert isinstance(svc_def, ServiceDefinition)
    assert svc_def.service_name == "sparkyidverify"
    assert svc_def.service_nice_name == "Sparky Identity Verification Service"
    assert (
        svc_def.service_instance_class_name
        == "com.accertify.service.external.vendor.sparky.idverify.SparkyIdentityVerificationService"
    )
    assert (
        svc_def.service_worker_instance_class_name
        == "com.accertify.service.external.vendor.sparky.idverify.SparkyIdentityVerificationServiceWorker"
    )
    assert svc_def.is_external_service


def test_load_from_file_handle() -> None:
    r, svc_defs = ServiceDefinitions.load_from_file(open(TEST_XML_FILE_2, "rt"))
    assert r
    assert isinstance(svc_defs, ServiceDefinitions)
    assert len(svc_defs) == 2

    r, svc_def = svc_defs.get("wanky")
    assert not r
    assert isinstance(svc_def, list)
    assert len(svc_def) == 1
    assert svc_def[0] == "Not a service: wanky"

    r, svc_def = svc_defs.get("sparkyidverify")
    assert r
    assert isinstance(svc_def, ServiceDefinition)


def test_big_load() -> None:
    r, svc_defs = ServiceDefinitions.load_from_file(open(REAL_XML_FILE, "rt"))
    assert r
    assert isinstance(svc_defs, ServiceDefinitions)
    assert 0 < len(svc_defs) < 1000


def test_service_names_all() -> None:
    r, svc_defs = ServiceDefinitions.load_from_file(TEST_XML_FILE_2)
    assert r
    assert isinstance(svc_defs, ServiceDefinitions)

    names = svc_defs.service_names()
    assert isinstance(names, set)
    assert len(names) == 2
    assert "sparkyidverify" in names
    assert "malarkyidverify" in names


def test_service_names_some() -> None:
    r, svc_defs = ServiceDefinitions.load_from_file(TEST_XML_FILE_2)
    assert r
    assert isinstance(svc_defs, ServiceDefinitions)

    names = svc_defs.service_names(pattern=".*verify")
    assert isinstance(names, set)
    assert len(names) == 2
    assert "sparkyidverify" in names
    assert "malarkyidverify" in names

    names = svc_defs.service_names(pattern="sparky.*")
    assert isinstance(names, set)
    assert len(names) == 1
    assert "sparkyidverify" in names
    assert "malarkyidverify" not in names


def test_service_names_fuzzy() -> None:
    r, svc_defs = ServiceDefinitions.load_from_file(TEST_XML_FILE_2)
    assert r
    assert isinstance(svc_defs, ServiceDefinitions)

    names = svc_defs.service_names(pattern="verify", fuzzy=True)
    assert isinstance(names, set)
    assert len(names) == 2
    assert "sparkyidverify" in names
    assert "malarkyidverify" in names

    names = svc_defs.service_names(pattern="sparky.*", fuzzy=True)
    assert isinstance(names, set)
    assert len(names) == 1
    assert "sparkyidverify" in names
    assert "malarkyidverify" not in names

    names = svc_defs.service_names(pattern="arkkyidv", fuzzy=True)
    assert isinstance(names, set)
    assert len(names) == 2
    assert "sparkyidverify" in names
    assert "malarkyidverify" in names

    names = svc_defs.service_names(pattern="sporky", fuzzy=True)
    assert isinstance(names, set)
    assert len(names) == 1
    assert "sparkyidverify" in names
    assert "malarkyidverify" not in names

    names = svc_defs.service_names(pattern="molarky", fuzzy=True)
    assert isinstance(names, set)
    assert len(names) == 1
    assert "sparkyidverify" not in names
    assert "malarkyidverify" in names


def test_is_service():
    r, svc_defs = ServiceDefinitions.load_from_file(TEST_XML_FILE_2)
    assert r
    assert isinstance(svc_defs, ServiceDefinitions)

    assert not svc_defs.is_service("wonky")
    assert svc_defs.is_service("sparkyidverify")
    assert svc_defs.is_service("malarkyidverify")


def test_is_external_service():
    r, svc_defs = ServiceDefinitions.load_from_file(TEST_XML_FILE_2)
    assert r
    assert isinstance(svc_defs, ServiceDefinitions)

    assert not svc_defs.is_external_service("wonky")
    assert svc_defs.is_external_service("sparkyidverify")
    assert not svc_defs.is_external_service("malarkyidverify")
