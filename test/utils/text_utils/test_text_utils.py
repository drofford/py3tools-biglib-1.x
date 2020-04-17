from biglib.utils.text_utils import pluralize

def test_basic_stuff():
    expect = "There is 1 thing"
    actual = pluralize("There {verb} {count} {noun}", verbs=("are", "is"), nouns=("things", "thing"), count=1)
    assert actual == expect

    expect = "There are 2 things"
    actual = pluralize("There {verb} {count} {noun}", verbs=("are", "is"), nouns=("things", "thing"), count=2)
    assert actual == expect

def test_more_singular():
    expect = "They have 1 gateau"
    actual = pluralize("They {verb} {count} {noun}", verbs=("have", "have"), nouns=("gateaux", "gateau"), count=1)
    assert actual == expect

    expect = "They have 1 gateau"
    actual = pluralize("They {verb} {count} {noun}", verbs=("have",), nouns=("gateaux", "gateau"), count=1)
    assert actual == expect

    expect = "They have 1 gateau"
    actual = pluralize("They {verb} {count} {noun}", verbs="have", nouns=("gateaux", "gateau"), count=1)
    assert actual == expect

def test_more_plural():
    expect = "They have 42 gateaux"
    actual = pluralize("They {verb} {count} {noun}", verbs=("have", "have"), nouns=("gateaux", "gateau"), count=42)
    assert actual == expect

    expect = "They have 42 gateaux"
    actual = pluralize("They {verb} {count} {noun}", verbs=("have",), nouns=("gateaux", "gateau"), count=42)
    assert actual == expect

    expect = "They have 42 gateaux"
    actual = pluralize("They {verb} {count} {noun}", verbs="have", nouns=("gateaux", "gateau"), count=42)
    assert actual == expect
