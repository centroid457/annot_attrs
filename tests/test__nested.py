import pytest
from pytest_aux import *

from annot_attrs import *


# =====================================================================================================================
class Victim1(AnnotsNested):
    ATTR1: int
    ATTR2: int = 2
    ATTR01 = 11


class Victim2(Victim1):
    ATTR3: int
    ATTR4: int = 4
    ATTR02 = 22


# =====================================================================================================================
def test__nested():
    victim1 = Victim1()
    victim2 = Victim2()

    assert list(victim1.annotations__get_nested()) == ['ATTR1', "ATTR2"]
    assert list(victim2.annotations__get_nested()) == ['ATTR1', "ATTR2", 'ATTR3', "ATTR4"]

    assert list(victim1.annotations__get_nested(victim1)) == ['ATTR1', "ATTR2"]
    assert list(victim1.annotations__get_nested(Victim2)) == ['ATTR1', "ATTR2", 'ATTR3', "ATTR4"]

    assert list(victim2.annotations__get_nested(victim1)) == ['ATTR1', "ATTR2"]
    assert list(victim2.annotations__get_nested(Victim2)) == ['ATTR1', "ATTR2", 'ATTR3', "ATTR4"]

    assert list(AnnotsNested.annotations__get_nested(victim1)) == ['ATTR1', "ATTR2"]
    assert list(AnnotsNested.annotations__get_nested(Victim2)) == ['ATTR1', "ATTR2", 'ATTR3', "ATTR4"]


# =====================================================================================================================
