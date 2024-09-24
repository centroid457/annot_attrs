# =====================================================================================================================
# VERSION = (0, 0, 1)   # use import EXACT_OBJECTS! not *
#   from .main import *                 # INcorrect
#   from .main import EXACT_OBJECTS     # CORRECT


# =====================================================================================================================
# TEMPLATE
# from .main import (
#     # BASE
#     EXACT_OBJECTS,
#
#     # AUX
#
#     # TYPES
#
#     # EXX
# )
# ---------------------------------------------------------------------------------------------------------------------
from .annots_nested import (
    # BASE
    AnnotsNested,
    IterAnnotValues,
    # AUX
    # TYPES
    # EXX
)
from .annot_attr import (
    # BASE
    AnnotAttrs,
    # AUX
    # TYPES
    # EXX
    Exx__AttrNotExist,
)
from .keys_as_values import (
    # BASE
    AnnotsClsKeysAsValues,
    # AUX
    AnnotsClsKeysAsValues_Meta,
    # TYPES
    # EXX
)

# =====================================================================================================================
