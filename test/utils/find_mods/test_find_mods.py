import importlib
# import logging
import os
import pkgutil
import sys
from pkgutil import ModuleInfo

from biglib import logger
from biglib.utils.find_mods import find_modules


def test_find_mods():
    logger.debug("sparky :: test_find_mods.py :: test_find_mods()")

    checks = []

    def do(mod_full_name: str, mod_info: ModuleInfo, sub_mod_data: object) -> None:
        checks.append(
            {
                "mod_full_name": mod_full_name,
                "mod_info": mod_info,
                "sub_mod_data": sub_mod_data,
                "result": None,
                "description": sub_mod_data.description()
                if "description" in dir(sub_mod_data)
                else mod_info.name,
            }
        )

    find_modules(
        "test.utils.sparky", when=lambda fn, mi: mi.name.startswith("check_"), do=do
    )

    result = True

    tests_run = 0
    tests_passed = 0
    tests_failed = 0

    for check in checks:
        mod_info = check["mod_info"]
        sub_mod_data = check["sub_mod_data"]
        desc = check["description"]

        if "pre" in dir(sub_mod_data):
            sub_mod_data.pre()

        if "do" in dir(sub_mod_data):
            b = sub_mod_data.do()
            tests_run += 1
            if b:
                tests_passed += 1
                rs = "passed"
            else:
                tests_failed += 1
                rs = "failed"
            check["result"] = rs

            logger.info(f"{desc} : {rs}")
            result = result and b

        if "post" in dir(sub_mod_data):
            sub_mod_data.post()

    assert tests_run == 4
    assert tests_passed == 4
    assert tests_failed == 0

    if tests_run == 0:
        print("ERROR: No checks were performed")
    else:
        print("")
        print(f"================================")
        print(f"===       TEST RESULTS       ===")
        print(f"--------------------------------")
        print(f"number of checks executed: {tests_run:5}")
        print(f"number of checks passed  : {tests_passed:5}")
        print(f"number of checks failed  : {tests_failed:5}")
        print(f"--------------------------------")
        if tests_failed == 0:
            print("All checks passed")
        elif tests_passed == 0:
            print("All checks failed")
        else:
            print("Some, but not all, checks passed")
        print(f"================================")
        print("")

        assert tests_run == tests_passed
