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
    def test__annots_set(self):
        class Cls(AnnotAttrs):
            ATTR1: int
            ATTR2: Optional[int] = None

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


# =====================================================================================================================
