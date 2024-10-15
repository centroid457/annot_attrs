from typing import *

from classes_aux import *

from .annot_aux import AnnotAux


# =====================================================================================================================
class Exx__AnnotNotDefined(Exception):
    """Exception in case of not defined attribute in instance
    """
    pass


# ---------------------------------------------------------------------------------------------------------------------
class AnnotAllDefined(AnnotAux):
    """Check all annotated and not defined attributes in instance obtain values!

    # IS IT STILL USED???
    DONT INHERIT with typing.NamedTuple! will raise!                ???
    For NamedTuple use as separated function with obj parameter!    ???
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # check ------------------------------------
        dict_type = self.annot__get_nested__dict_types()
        not_defined = self.annot__get_not_defined()
        if not_defined:
            msg = f"[CRITICAL]{not_defined=} in {dict_type}"
            raise Exx__AnnotNotDefined(msg)

    # TODO: deside is it really need NamedTuple and dataclasses??? seems its not need!!!

    # def annots_get_set(self, obj: Optional[Any] = None) -> Set[str]:
    #     """get undefined annotated attributes in class (not instance!)
    #     """
    #     annots = set()
    #     if obj is None:
    #         obj = self
    #     mro = obj.__class__.__mro__
    #     for cls in mro[:-1]:
    #         if cls == tuple and hasattr(obj, "_fields"):    # NamedTuple
    #             return set(obj._fields).difference(set(obj._field_defaults))
    #         if not hasattr(cls, "__annotations__"):     # for last class (tuple) in NamedTuple!
    #             continue
    #         for name in set(cls.__annotations__):
    #             if not hasattr(cls, name):
    #                 annots.update({name, })
    #     # print(annots)
    #     return annots
    #
    # def annots_get_dict(self, obj: Optional[Any] = None) -> Union[Dict[str, Any], NoReturn]:
    #     """get dict of undefined annotated attributes in class but defined in instance!
    #     """
    #     annots = dict()
    #     for name in self.annots_get_set(obj):
    #         annots.update({name: self.attr_get_case_insensitive(name, obj)})
    #     return annots
    #
    # def annots_get_values(self, obj: Optional[Any] = None) -> Union[Iterable[Any], NoReturn]:
    #     """get iterable values of undefined annotated attributes in class but defined in instance!
    #     """
    #     return self.annots_get_dict(obj).values()
    #
    # def attr_get_case_insensitive(self, name: str, obj: Optional[Any] = None) -> Union[str, NoReturn]:
    #     """get value for attr name without case sense.
    #     if no attr name in source - raise!
    #     """
    #     if obj is None:
    #         obj = self
    #
    #     attrs_all = list(filter(lambda attr: not callable(getattr(obj, attr)) and not attr.startswith("__"), dir(obj)))
    #
    #     attrs_similar = list(filter(lambda attr: attr.lower() == name.lower(), attrs_all))
    #     if len(attrs_similar) == 1:
    #         return getattr(obj, attrs_similar[0])
    #     elif len(attrs_similar) == 0:
    #         msg = f"[CRITICAL]no[{name=}] in any cases [{attrs_all=}]"
    #         raise Exx__AnnotNotDefined(msg)
    #     else:
    #         msg = f"[CRITICAL]exists several similar [{attrs_similar=}]"
    #         raise Exx__AnnotNotDefined(msg)


# =====================================================================================================================
