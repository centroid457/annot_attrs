# annot_attrs
Designed to get list of annotated but not defined/not used attrs from class (not instance!).  
may be helpful further in instance to check that really have values.

## Features
1. get set of unused attributes from class(not instance!)
2. work with nested classes
3. get values 
   * by case insensitive names
   * by dict key access method
4. work on any object (over Obj parameter!)  
at least for NamedTuple


## License
See the [LICENSE](LICENSE) file for license rights and limitations (MIT).


## Release history
See the [HISTORY.md](HISTORY.md) file for release history.


## Installation
```commandline
pip install annot-attrs
```

## Import

```python
from annot_attrs import *
```


## GUIDE

### 1. inheritance

```python
from annot_attrs import *


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



assert Cls().ATTR2 == 2
assert Cls().attr2 == 2
        
assert Cls()["ATTR2"] == 2
assert Cls()["attr2"] == 2



obj = Cls()
try:
    obj.annots_get_dict()
except Exx_AttrNotExist:
    pass
else:
    assert False

obj.ATTR1 = 1
assert obj.annots_get_dict() == {"ATTR1": 1}
```

### 2. Indepandant usage
```python
from annot_attrs import *

try:
    class Cls(AnnotAttrs, NamedTuple):
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
assert AnnotAttrs().annots_get_set(obj) == {"ATTR1", }
assert AnnotAttrs().annots_get_dict(obj) == {"ATTR1": 1}
```
