# =====================================================================================================================
# VERSION = (0, 0, 1)   # use import EXACT_OBJECTS! not *
#   from .main import *                 # INcorrect
#   from .main import EXACT_OBJECTS     # CORRECT
# VERSION = (0, 0, 2)   # del blank lines
# VERSION = (0, 0, 3)   # separate all types/exx into static.py!


# =====================================================================================================================
# TEMPLATE
# from .STATIC import (
#     # TYPES
#     # EXX
# )
# from .main import (
#     # BASE
#     # AUX
# )
# ---------------------------------------------------------------------------------------------------------------------
from .static import (
    # TYPES
    # EXX
    Exx__AnnotNotDefined,
)
from .annot_aux import (
    # BASE
    AnnotAux,
    # AUX
)
from .annot_iter_values import AnnotValuesIter
from .annot_all_defined import (
    # BASE
    AnnotAllDefined,
    # AUX
)
from .annot_cls_keys_as_values import (
    # BASE
    AnnotClsKeysAsValues,
    # AUX
    AnnotClsKeysAsValues_Meta,
)

# =====================================================================================================================
