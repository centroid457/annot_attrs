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


victim1 = Victim1()
victim2 = Victim2()


# =====================================================================================================================
@pytest.mark.parametrize(
    argnames="asker, source, _EXPECTED",
    argvalues=[
        (victim1, None, ['ATTR1', "ATTR2"]),
        (victim2, None, ['ATTR1', "ATTR2", 'ATTR3', "ATTR4"]),

        (victim1, victim1, ['ATTR1', "ATTR2"]),
        (victim2, victim2, ['ATTR1', "ATTR2", 'ATTR3', "ATTR4"]),

        (victim2, victim1, ['ATTR1', "ATTR2"]),
        (victim1, victim2, ['ATTR1', "ATTR2", 'ATTR3', "ATTR4"]),

        (AnnotsNested, victim1, ['ATTR1', "ATTR2"]),
        (AnnotsNested, victim2, ['ATTR1', "ATTR2", 'ATTR3', "ATTR4"]),
    ]
)
def test__annots_nested(asker, source, _EXPECTED):
    func_link = lambda x: list(x.annotations__get_nested(source))
    pytest_func_tester__no_kwargs(func_link, asker, _EXPECTED)


# =====================================================================================================================
class VictimIter(Victim2, IterAnnotValues):
    pass


def test__nested_iter():
    assert list(VictimIter()) == [2, 4]


# =====================================================================================================================
