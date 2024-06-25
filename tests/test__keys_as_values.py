import pytest
from pytest_aux import *

from annot_attrs import *


# =====================================================================================================================
class Victim(AnnotsClsKeysAsValues):
    ATTR1: str
    ATTR2: str
    ATTR3: str


Victim_VALUES = ["ATTR1", "ATTR2", "ATTR3"]


# =====================================================================================================================
@pytest.mark.parametrize(
    argnames="args, _EXPECTED",
    argvalues=[
        ("ATTR1", "ATTR1"),
        ("attr1", AttributeError),

        ("ATTR2", "ATTR2"),
        ("notExists", AttributeError),
        ("use spaces", AttributeError),
    ]
)
def test__values(args, _EXPECTED):
    func_link = lambda value: getattr(Victim, value)
    pytest_func_tester__no_kwargs(func_link, args, _EXPECTED)


@pytest.mark.parametrize(
    argnames="args, _EXPECTED",
    argvalues=[
        (0, "ATTR1"),
        (1, "ATTR2"),
        (2, "ATTR3"),
        (3, IndexError),
        (-1, "ATTR3"),
        (-2, "ATTR2"),
        (-3, "ATTR1"),
        (-4, IndexError),
    ]
)
def test__geitem(args, _EXPECTED):
    func_link = lambda value: Victim[value]
    pytest_func_tester__no_kwargs(func_link, args, _EXPECTED)


def test__iter():
    assert list(Victim) == Victim_VALUES


def test__len():
    assert len(Victim) == len(Victim_VALUES)


def test__in():
    assert "attr1" not in Victim
    assert "ATTR1" in Victim
    assert "ATTR2" in Victim


# =====================================================================================================================
