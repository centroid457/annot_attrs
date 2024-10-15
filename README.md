![Ver/TestedPython](https://img.shields.io/pypi/pyversions/annot_attrs)
![Ver/Os](https://img.shields.io/badge/os_development-Windows-blue)  
![repo/Created](https://img.shields.io/github/created-at/centroid457/annot_attrs)
![Commit/Last](https://img.shields.io/github/last-commit/centroid457/annot_attrs)
![Tests/GitHubWorkflowStatus](https://github.com/centroid457/annot_attrs/actions/workflows/test_linux.yml/badge.svg)
![Tests/GitHubWorkflowStatus](https://github.com/centroid457/annot_attrs/actions/workflows/test_windows.yml/badge.svg)  
![repo/Size](https://img.shields.io/github/repo-size/centroid457/annot_attrs)
![Commit/Count/t](https://img.shields.io/github/commit-activity/t/centroid457/annot_attrs)
![Commit/Count/y](https://img.shields.io/github/commit-activity/y/centroid457/annot_attrs)
![Commit/Count/m](https://img.shields.io/github/commit-activity/m/centroid457/annot_attrs)

# annot_attrs (current v0.0.13/![Ver/Pypi Latest](https://img.shields.io/pypi/v/annot_attrs?label=pypi%20latest))

## DESCRIPTION_SHORT
work with annotated but not defined/not used attrs in class

## DESCRIPTION_LONG
Designed to get list of annotated but not defined/not used attrs from class (not instance!).  
    may be helpful further in instance to check that really have values.


## Features
1. get set of unused attributes from class(not instance!)  
2. work with nested classes  
3. get values:  
	- by case insensitive names  
	- by dict key access method  
4. work on any object (over Obj parameter!):  
	- at least for NamedTuple  


********************************************************************************
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


********************************************************************************
## USAGE EXAMPLES
See tests, sourcecode and docstrings for other examples.  

------------------------------
### 1. example1.py

```python
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
```

********************************************************************************
