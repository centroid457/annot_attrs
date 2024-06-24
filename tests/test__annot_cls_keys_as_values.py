from typing import *
import pathlib

import pytest
from pytest import mark
from pytest_aux import *

from annot_attrs import *


# =====================================================================================================================
class Victim(AnnotsClsKeysAsValues):
    TRUE: str
    FALSE: str
    NONE: str


Victim_VALUES = ["TRUE", "FALSE", "NONE"]


# =====================================================================================================================
@pytest.mark.parametrize(
    argnames="args, _EXPECTED",
    argvalues=[
        ("TRUE", "TRUE"),
        ("True", AttributeError),
        ("true", AttributeError),

        ("FALSE", "FALSE"),
        ("NONE", "NONE"),

        ("meth", AttributeError),
    ]
)
def test__values(args, _EXPECTED):
    func_link = lambda value: getattr(Victim, value)
    pytest_func_tester__no_kwargs(func_link, args, _EXPECTED)


def test__iter():
    assert list(Victim) == Victim_VALUES


def test__len():
    assert len(Victim) == len(Victim_VALUES)


def test__in():
    assert "true" not in Victim
    assert "TRUE" in Victim
    assert "FALSE" in Victim
    assert "NONE" in Victim


# =====================================================================================================================
