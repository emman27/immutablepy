from immutable import Dict


def test_str():
    """
    Renders correctly on str
    """
    assert str(Dict({'a': 1})) == "{'a': 1}"


def test_getitem():
    """
    Allows the getting of a key
    """
    d = Dict({'a': 1})
    assert d['a'] == 1


def test_equality():
    """
    Dicts are equal if the underlying dictionaries are equal
    """
    assert Dict() == Dict()
    assert Dict({'a': 1}) == Dict({'a': 1})
    assert Dict() != Dict({'a': 1})