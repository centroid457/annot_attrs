from typing import *


# =====================================================================================================================
class AnnotsNested:
    """
    access to all __annotations__
        from all nested classes
        in correct order

    RULES
    -----
    4. nesting available with correct order!
        class ClsFirst(BreederStrStack):
            atr1: int
            atr3: int = None

        class ClsLast(BreederStrStack):
            atr2: int = None
            atr4: int

        for key, value in ClsLast.annotations__get_nested_list().items():
            print(f"{key}:{value}")

        # atr1:<class 'int'>
        # atr3:<class 'int'>
        # atr2:<class 'int'>
        # atr4:<class 'int'>
    """
    @classmethod
    def annotations__get_nested(cls, obj: Any | None = None) -> dict[str, Any]:
        """
        get all annotations in correct order!
        """
        if obj is None:
            obj = cls

        try:
            mro = obj.__mro__
        except:
            mro = obj.__class__.__mro__

        result = {}
        for cls_i in mro:
            if cls_i == AnnotsNested or cls_i == object:
                break

            result = dict(**cls_i.__annotations__, **result)
        return result


# =====================================================================================================================
