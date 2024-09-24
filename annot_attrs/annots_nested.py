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

        for key, value in ClsLast.annotations__get_nested().items():
            print(f"{key}:{value}")

        # atr1:<class 'int'>
        # atr3:<class 'int'>
        # atr2:<class 'int'>
        # atr4:<class 'int'>
    """
    @classmethod
    def annotations__get_nested(cls, obj: Any | None = None) -> dict[str, Type[Any]]:
        """
        GOAL
        ----
        get all annotations in correct order (nesting available)!

        RETURN
        ------
        keys - all attr names (defined and not)
        values - Types!!! not instances!!!
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
class IterAnnotValues(AnnotsNested):
    """
    GOAL
    ----
    iterate annot defined values in position order(nesting is available)

    USAGE
    -----
        class Item:
            pass

        class Example(IterAnnotValues):
            def meth(self):
                pass

            VALUE1: Item = Item(1)
            VALUE3: Item = Item(3)
            VALUE2: Item = Item(2)
            VALUE20: Item
            VALUE200 = 200

        for i in Example():
            print(i)

        ---> Item(1), Item(3), Item(2)

    SPECIALLY CREATED FOR
    ---------------------
    pyqt_templates.pte_highlights.StylesPython

    """

    def __iter__(self):
        for key in self.annotations__get_nested():
            if hasattr(self, key):
                yield getattr(self, key)


# =====================================================================================================================
