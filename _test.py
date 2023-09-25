import os
import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory
from typing import *
from configparser import ConfigParser
from dataclasses import dataclass

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

    def test__annots_get_values(self):
        class Cls(AnnotAttrs):
            ATTR1: int
            ATTR2: int = 2

        obj = Cls()
        obj.ATTR1 = 1
        assert list(obj.annots_get_values()) == [1, ]

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

    # -----------------------------------------------------------------------------------------------------------------
    def test__obj(self):
        class Cls:
            ATTR1: int
            ATTR2: int = 2

        obj = Cls()
        obj.ATTR1 = 1

        assert AnnotAttrs().annots_get_set(obj) == {"ATTR1", }
        assert AnnotAttrs().annots_get_dict(obj) == {"ATTR1": 1}

    # -----------------------------------------------------------------------------------------------------------------
    def test__NamedTuple(self):
        try:
            class Cls(AnnotAttrs, NamedTuple):
                ATTR1: int
                ATTR2: int = 2
        except TypeError:
            # TypeError: can only inherit from a NamedTuple type and Generic
            pass
        else:
            assert True

    def test__NamedTuple_by_obj(self):
        class Cls(NamedTuple):
            ATTR1: int
            ATTR2: int = 2

        obj = Cls(1)

        assert AnnotAttrs().annots_get_set(obj) == {"ATTR1", }
        assert AnnotAttrs().annots_get_dict(obj) == {"ATTR1": 1, }

    # -----------------------------------------------------------------------------------------------------------------
    def test__dataclass(self):
        @dataclass
        class Cls(AnnotAttrs):
            ATTR1: int
            ATTR2: int = 2

        assert Cls(1).annots_get_set() == {"ATTR1", }
        assert Cls(1).annots_get_dict() == {"ATTR1": 1, }

    def test__dataclass_by_obj(self):
        # 10------------------
        @dataclass
        class Cls:
            ATTR1: int
            ATTR2: int = 2

        class Cls2(Cls):
            ATTR2: int = 22
            ATTR3: int = 33

        obj = Cls2(1)
        assert AnnotAttrs().annots_get_set(obj) == {"ATTR1", }
        assert AnnotAttrs().annots_get_dict(obj) == {"ATTR1": 1, }

        # 01------------------
        class Cls:
            ATTR1: int
            ATTR2: int = 2

        @dataclass
        class Cls2(Cls):
            ATTR2: int = 22
            ATTR3: int = 33

        obj = Cls2(1)
        assert AnnotAttrs().annots_get_set(obj) == {"ATTR1", }
        try:
            assert AnnotAttrs().annots_get_dict(obj) == {"ATTR1": 1, }
        except Exx_AttrNotExist:
            pass   # its GOOD!!!
        else:
            assert False

        # 11------------------
        @dataclass
        class Cls:
            ATTR1: int
            ATTR2: int = 2

        @dataclass
        class Cls2(Cls):
            ATTR2: int = 22
            ATTR3: int = 33

        obj = Cls2(1)
        assert AnnotAttrs().annots_get_set(obj) == {"ATTR1", }
        assert AnnotAttrs().annots_get_dict(obj) == {"ATTR1": 1, }

    def test__PROPERTY_w_ITER_w_VALUES(self):
        # 1---------------------------------------------------------
        # this will work correct
        class Cls:
            ATTR1: int
            ATTR2: int = 2

            @property
            def meth_as_property(self):
                return 333

        obj = Cls()
        obj.ATTR1 = 1

        assert AnnotAttrs().annots_get_set(obj) == {"ATTR1", }
        assert AnnotAttrs().annots_get_dict(obj) == {"ATTR1": 1, }
        assert list(AnnotAttrs().annots_get_values(obj)) == [1, ]

        # 2---------------------------------------------------------
        # this will RAISE!
        class Cls:
            ATTR1: int
            ATTR2: int = 2

            @property
            def meth_as_property(self):
                return sum(self)

            def __iter__(self):
                yield from AnnotAttrs().annots_get_values(self)

        obj = Cls()
        obj.ATTR1 = 1

        assert AnnotAttrs().annots_get_set(obj) == {"ATTR1", }

        try:
            assert AnnotAttrs().annots_get_dict(obj) == {"ATTR1": 1, }
            # assert list(AnnotAttrs().annots_get_values(obj)) == [1, ]
        except RecursionError:
            pass
        else:
            assert False

        # 3 FIXED---------------------------------------------------------
        # this will work correct!
        class Cls:
            ATTR1: int
            ATTR2: int = 2

            def meth_NO_property(self):
                return sum(self)

            def __iter__(self):
                yield from AnnotAttrs().annots_get_values(self)

        obj = Cls()
        obj.ATTR1 = 1

        assert AnnotAttrs().annots_get_set(obj) == {"ATTR1", }
        assert AnnotAttrs().annots_get_dict(obj) == {"ATTR1": 1, }
        assert list(AnnotAttrs().annots_get_values(obj)) == [1, ]


# =====================================================================================================================
