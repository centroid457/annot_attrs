import os
import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory
from typing import *
from configparser import ConfigParser

from annot_attrs import *


# =====================================================================================================================
class Test:
    # -----------------------------------------------------------------------------------------------------------------
    def test__annots_get_set(self):
        class Cls(AnnotAttrs):
            ATTR1: int
            ATTR2: int = 2

        assert Cls().annots_get_set() == {"ATTR1", }

        class Cls2(Cls):
            ATTR1: int = 2
            ATTR3: int

        assert Cls2().annots_get_set() == {"ATTR1", "ATTR3", }

        inst = Cls2()
        inst.ATTR1 = 1
        inst.ATTR2 = 1
        inst.ATTR3 = 1

        assert Cls2().annots_get_set() == {"ATTR1", "ATTR3", }

    def test__annots_get_dict(self):
        class Cls(AnnotAttrs):
            ATTR1: int
            ATTR2: int = 2

        obj = Cls()
        try:
            obj.annots_get_dict()
        except Exx_AttrNotExist:
            pass
        else:
            assert False

        obj.ATTR1 = 1
        assert obj.annots_get_dict() == {"ATTR1": 1}

    def test__getattr(self):
        class Cls(AnnotAttrs):
            ATTR1: int
            ATTR2: int = 2

        assert Cls().ATTR2 == 2
        assert Cls().attr2 == 2

        try:
            Cls().ATTR222
        except Exx_AttrNotExist:
            pass
        else:
            assert False

    def test__getitem(self):
        class Cls(AnnotAttrs):
            ATTR1: int
            ATTR2: int = 2

        assert Cls()["ATTR2"] == 2
        assert Cls()["attr2"] == 2

        try:
            Cls()["ATTR222"]
        except Exx_AttrNotExist:
            pass
        else:
            assert False


# =====================================================================================================================
