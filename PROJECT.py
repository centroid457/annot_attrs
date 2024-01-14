from typing import *


# =====================================================================================================================
class PROJECT:
    # AUX --------------------------------------------------
    _VERSION_TEMPLATE: Tuple[int] = (0, 0, 1)

    # AUTHOR -----------------------------------------------
    AUTHOR_NAME: str = "Andrei Starichenko"
    AUTHOR_EMAIL: str = "centroid@mail.ru"
    AUTHOR_HOMEPAGE: str = "https://github.com/centroid457/"

    # PROJECT ----------------------------------------------
    NAME_INSTALL: str = "annot-attrs"
    NAME_IMPORT: str = "annot_attrs"
    KEYWORDS: List[str] = [
        "annotations", "annots",
        "not defined attributes", "attributes"
    ]

    # GIT --------------------------------------------------
    DESCRIPTION_SHORT: str = "work with annotated but not defined/not used attrs in class"

    # README -----------------------------------------------
    pass

    # add DOUBLE SPACE at the end of all lines! for correct representation in MD-viewers
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
    VERSION: Tuple[int, int, int] = (0, 0, 4)
    VERSION_STR: str = ".".join(map(str, VERSION))
    TODO: List[str] = [
        "..."
    ]
    FIXME: List[str] = [
        "..."
    ]
    NEWS: List[str] = [
        "apply new pypi template"
    ]


# =====================================================================================================================
if __name__ == '__main__':
    pass


# =====================================================================================================================
