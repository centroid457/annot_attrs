# annot_attrs
Designed to get list of annotated but not defined/not used attrs from class (not instance!).  
may be helpful further in instance to check that really have values.

## Features
1. get set of unused attributes from class(not instance!)
2. work with nested classes
3. get values 
   * by case insensitive names
   * by dict key access method


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
