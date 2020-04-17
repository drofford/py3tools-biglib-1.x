from biglib.utils.locations import Locations


def test_get_interceptas_root():

    r, t1 = Locations.get_interceptas_root_dir()
    assert r
    assert t1 == "/Users/gofford/projects/interceptas"

    r, t2 = Locations.get_interceptas_root_dir()
    assert r
    assert t2 == "/Users/gofford/projects/interceptas"
    assert t2 == t1


def test_get_vertigo_root():

    r, t1 = Locations.get_vertigo_root_dir()
    assert r
    assert t1 == "/Users/gofford/projects/vertigo"

    r, t2 = Locations.get_vertigo_root_dir()
    assert r
    assert t2 == "/Users/gofford/projects/vertigo"
    assert t2 == t1


def test_get_service_definitions_path():

    r, t1 = Locations.get_service_definitions_path()
    assert r
    assert t1 == "/Users/gofford/projects/vertigo/src/resources/serviceDefinitions.xml"

    r, t2 = Locations.get_service_definitions_path()
    assert r
    assert t2 == "/Users/gofford/projects/vertigo/src/resources/serviceDefinitions.xml"
    assert t2 == t1


def test_get_master_properties_path():

    r, t1 = Locations.get_service_definitions_path()
    assert r
    assert t1 == "/Users/gofford/projects/vertigo/src/resources/serviceDefinitions.xml"

    r, t2 = Locations.get_service_definitions_path()
    assert r
    assert t2 == "/Users/gofford/projects/vertigo/src/resources/serviceDefinitions.xml"
    assert t2 == t1

    r, t3 = Locations.get_master_properties_path()
    assert r

    r, t4 = Locations.get_master_properties_path()
    assert r
    assert t4 == t3


def get_application_properties_path():
    pass
