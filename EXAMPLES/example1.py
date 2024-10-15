# ===============================================================
### 1. inheritance
# (BEST practice - dont mess classes! use as separated object!)
from annot_attrs import *

class Cls:
    ATTR1: int
    ATTR2: int = 2

obj = Cls(1)

assert AnnotAllDefined().annots_get_set(obj) == {"ATTR1", }
assert AnnotAllDefined().annots_get_dict(obj) == {"ATTR1": 1, }


# ===============================================================
from annot_attrs import *

class Cls(AnnotAllDefined):
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

assert Cls().ATTR2 == 2
assert Cls().attr2 == 2

assert Cls()["ATTR2"] == 2
assert Cls()["attr2"] == 2

obj = Cls()
try:
    obj.annots_get_dict()
except Exx__AnnotNotDefined:
    pass
else:
    assert False

obj.ATTR1 = 1
assert obj.annots_get_dict() == {"ATTR1": 1}


# ===============================================================
### 2. Indepandant usage
from annot_attrs import *

try:
    class Cls(AnnotAllDefined, NamedTuple):
        ATTR1: int
        ATTR2: int = 2
except TypeError:
    # TypeError: can only inherit from a NamedTuple type and Generic
    pass
else:
    assert True

class Cls(NamedTuple):
    ATTR1: int
    ATTR2: int = 2

obj = Cls(1)
assert AnnotAllDefined().annots_get_set(obj) == {"ATTR1", }
assert AnnotAllDefined().annots_get_dict(obj) == {"ATTR1": 1}
