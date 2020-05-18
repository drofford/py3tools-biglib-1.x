from biglib.utils.text_utils import join


def test_empty():
    expect = '""'
    actual = join([])
    assert actual == expect

    expect = ""
    actual = join([], quoted=False)
    assert actual == expect

    expect = '""'
    actual = join([], separator="X")
    assert actual == expect

    expect = '""'
    actual = join([], oxford_comma=False)
    assert actual == expect

    expect = ""
    actual = join([], quoted=False, oxford_comma=False)
    assert actual == expect


def test_just_one():
    expect = '"john"'
    actual = join(["john"])
    assert actual == expect

    expect = "john"
    actual = join(["john"], quoted=False)
    assert actual == expect


def test_with_two():
    expect = '"john", "paul"'
    actual = join(["john", "paul"])
    assert actual == expect

    expect = '"john","paul"'
    actual = join(["john", "paul"], separator=",")
    assert actual == expect

    expect = '"john","paul"'
    actual = join(["john", "paul"], separator=",", oxford_comma=False)
    assert actual == expect

    expect = '"john" and "paul"'
    actual = join(["john", "paul"], conjunction="and")
    assert actual == expect

    expect = '"john" kaj "paul"'
    actual = join(["john", "paul"], conjunction="kaj")
    assert actual == expect

    expect = "john, paul"
    actual = join(["john", "paul"], quoted=False)
    assert actual == expect

    expect = "john and paul"
    actual = join(["john", "paul"], quoted=False, conjunction="and")
    assert actual == expect


def test_with_three():
    expect = '"john", "paul", "george"'
    actual = join(("john", "paul", "george"))
    assert actual == expect

    expect = "john, paul, george"
    actual = join(("john", "paul", "george"), quoted=False)
    assert actual == expect

    expect = "john, paul, and george"
    actual = join(("john", "paul", "george"), quoted=False, conjunction="and")
    assert actual == expect

    expect = "john, paul and george"
    actual = join(
        ("john", "paul", "george"), quoted=False, conjunction="and", oxford_comma=False
    )
    assert actual == expect

    expect = "john, paul, george"
    actual = join(("john", "paul", "george"), quoted=False, oxford_comma=False)
    assert actual == expect

    expect = "john, paul, george"
    actual = join(("john", "paul", "george"), quoted=False)
    assert actual == expect
