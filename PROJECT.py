from typing import *
from _aux__release_files import release_files_update


# =====================================================================================================================
VERSION = (0, 0, 3)   # 1/deprecate _VERSION_TEMPLATE from PRJ object +2/place update_prj here in __main__ +3/separate finalize attrs


# =====================================================================================================================
class PROJECT:
    # AUTHOR -----------------------------------------------
    AUTHOR_NAME: str = "Andrei Starichenko"
    AUTHOR_EMAIL: str = "centroid@mail.ru"
    AUTHOR_HOMEPAGE: str = "https://github.com/centroid457/"

    # PROJECT ----------------------------------------------
    NAME_IMPORT: str = "annot_attrs"
    KEYWORDS: List[str] = [
        "annotations", "annots",
        "not defined attributes", "attributes"
    ]
    CLASSIFIERS_TOPICS_ADD: List[str] = [
        # "Topic :: Communications",
        # "Topic :: Communications :: Email",
    ]

    # README -----------------------------------------------
    # add DOUBLE SPACE at the end of all lines! for correct representation in MD-viewers
    DESCRIPTION_SHORT: str = "work with annotated but not defined/not used attrs in class"
    DESCRIPTION_LONG: str = """
    Designed to get list of annotated but not defined/not used attrs from class (not instance!).  
    may be helpful further in instance to check that really have values.
        """
    FEATURES: List[str] = [
        # "feat1",
        # ["feat2", "block1", "block2"],

        "get set of unused attributes from class(not instance!)",
        "work with nested classes",
        ["get values", "by case insensitive names", "by dict key access method"],
        ["work on any object (over Obj parameter!)", "at least for NamedTuple"],
    ]

    # HISTORY -----------------------------------------------
    VERSION: Tuple[int, int, int] = (0, 0, 7)
    TODO: List[str] = [
        "..."
    ]
    FIXME: List[str] = [
        "..."
    ]
    NEWS: List[str] = [
        "[__INIT__.py] fix import",
        "apply last pypi template",
    ]

    # FINALIZE -----------------------------------------------
    VERSION_STR: str = ".".join(map(str, VERSION))
    NAME_INSTALL: str = NAME_IMPORT.replace("_", "-")


# =====================================================================================================================
if __name__ == '__main__':
    release_files_update(PROJECT)


# =====================================================================================================================
