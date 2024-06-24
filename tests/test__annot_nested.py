from typing import *
import pathlib

import pytest
from pytest import mark
from pytest_aux import *

from annot_attrs import *


# =====================================================================================================================
class Test:
    @classmethod
    def setup_class(cls):
        cls.Victim = AnnotsNested

    # # @classmethod
    # # def teardown_class(cls):
    # #     pass
    # #
    # def setup_method(self, method):
    #     pass
    #
    # def teardown_method(self, method):
    #     pass
    # -----------------------------------------------------------------------------------------------------------------
    def test__1(self):
        class Victim1(self.Victim):
            ATTR1: int
            ATTR2: int = 2
            ATTR01 = 11

        class Victim2(Victim1):
            ATTR3: int
            ATTR4: int = 4
            ATTR02 = 22

        # SINGLE --------------------
        victim1 = Victim1()
        assert list(victim1.annotations__get_nested()) == ['ATTR1', "ATTR2"]

        assert list(victim1.annotations__get_nested(victim1)) == ['ATTR1', "ATTR2"]
        assert list(victim1.annotations__get_nested(Victim1)) == ['ATTR1', "ATTR2"]

        assert list(AnnotsNested.annotations__get_nested(victim1)) == ['ATTR1', "ATTR2"]
        assert list(AnnotsNested.annotations__get_nested(Victim1)) == ['ATTR1', "ATTR2"]

        # NESTED --------------------
        victim2 = Victim2()
        assert list(victim2.annotations__get_nested()) == ['ATTR1', "ATTR2", 'ATTR3', "ATTR4"]

        assert list(victim2.annotations__get_nested(victim2)) == ['ATTR1', "ATTR2", 'ATTR3', "ATTR4"]
        assert list(victim2.annotations__get_nested(Victim2)) == ['ATTR1', "ATTR2", 'ATTR3', "ATTR4"]

        assert list(AnnotsNested.annotations__get_nested(victim2)) == ['ATTR1', "ATTR2", 'ATTR3', "ATTR4"]
        assert list(AnnotsNested.annotations__get_nested(Victim2)) == ['ATTR1', "ATTR2", 'ATTR3', "ATTR4"]


# =====================================================================================================================
