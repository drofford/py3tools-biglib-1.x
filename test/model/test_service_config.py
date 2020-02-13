import json
import logging
import os
import os.path
import py.test
import re
import sys

from biglib.model.service_config import ServiceConfig
from biglib.model.service_config_params import ServiceConfigParams
from test.model.helpers import _create_kiki


def test_load_file_raw():
    file = os.path.join("test", "data", "json", "CHECK.json")
    x = json.load(open(file, "rt"))
    logging.debug(f"{type(x)=}")
    logging.debug(f"{x=}")

    logging.debug(json.dumps(x, indent=4))

    # assert False


def test_load_file_not_found():
    file = os.path.join("test", "data", "json", "WONKY.json")
    r, t = ServiceConfig.load_from_file(file)
    assert not r
    assert isinstance(t, list)
    assert len(t) == 1
    assert t[0] == "no such file: test/data/json/WONKY.json"


def test_load_from_file_path():
    file = os.path.join(os.getcwd(), "test", "data", "json", "CHECK.json")
    logging.debug(f"test_load_from_file_path: file path = {file}")
    logging.debug(f"test_load_from_file_path: curdir= {os.getcwd()}")
    logging.debug(f"test_load_from_file_path: exists? {os.path.exists(file)}")
    logging.debug(f"test_load_from_file_path: isfile? {os.path.isfile(file)}")
    logging.debug(f"test_load_from_file_path: isdir ? {os.path.isdir(file)}")
    r, t = ServiceConfig.load_from_file(file)
    logging.debug(f"test_load_from_file_path: {r=}")
    logging.debug(f"test_load_from_file_path: {t=}")
    assert r
    assert isinstance(t, ServiceConfig)


def test_load_from_open_file():
    file = open(os.path.join("test", "data", "json", "CHECK.json"), "rt")
    r, t = ServiceConfig.load_from_file(file)
    assert r
    assert isinstance(t, ServiceConfig)


def test_parsed_service_config():
    file = open(os.path.join("test", "data", "json", "CHECK.json"), "rt")
    r, svc_cfg = ServiceConfig.load_from_file(file)
    assert r

    assert svc_cfg.service_config_version.version == "1"
    assert svc_cfg.service_config_method.method == "CHECK"

    assert svc_cfg.get_service_config_version() == (True, "1")
    assert svc_cfg.get_service_config_method() == (True, "CHECK")

    r, request_params = svc_cfg.get_service_request_params()
    logging.info(f"{type(request_params)=} {request_params=}")
    assert r
    assert request_params is not None
    assert isinstance(request_params, ServiceConfigParams)
    assert len(request_params) == 4
