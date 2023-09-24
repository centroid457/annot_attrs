# annot_attrs
Designed to get list of annotated but not defined/not used attrs from class (not instance!).  
may be helpful further in instance to check that really have values.

## Features
1. get list of unused attributes from class
2. work with nested classes


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
    ATTR2: Optional[int] = None

print(Cls().annots_list())  #[ATTR1, ]

class Cls2(Cls):
    ATTR1: int = 2
    ATTR3: int

print(Cls2().annots_list())  #[ATTR1, ATTR3, ]

inst = Cls2()
inst.ATTR1 = 1
inst.ATTR2 = 1
inst.ATTR3 = 1

print(inst.annots_list())  #[ATTR1, ATTR3, ]
```
