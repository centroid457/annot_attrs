from typing import *


# =====================================================================================================================
class Exx_AttrNotExist(Exception):
    """Exception in case of not existed attribute in instance
    """
    pass


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
            if cls_i == AnnotsNested:
                break

            result = dict(**cls_i.__annotations__, **result)
        return result


# =====================================================================================================================
class AnnotAttrs:
    """Check all annotated and not defined attributes in instance obtain values!

    DONT INHERIT with typing.NamedTuple! will raise!
    For NamedTuple use as separated function with obj parameter!
    """
    def __getattr__(self, item: str) -> Union[str, NoReturn]:
        """ability to access values by attribute with any letercase ClsInstance.key and *.KEY,
        it is important in this project because
        - from INI files python obtain names in lowercase
        - from ENV - in uppercase
        """
        if item in ["__isabstractmethod__", ]:
            return
        else:
            return self.attr_get_case_insensitive(item)

    def __getitem__(self, key: str) -> Union[str, NoReturn]:
        """ability to access values by dict style ClsInstance["key"]
        """
        return self.attr_get_case_insensitive(key)

    def __str__(self):
        """just a pretty string.
        """
        result = "AnnotAttrs:"
        data = self.annots_get_dict()
        if data:
            for key, value in data.items():
                result += f"\n{key}={value}"
        else:
            result += f"\ndata=None"
        return result

    def print(self) -> None:
        """just a pretty print for debugging or research.
        """
        print(self)

    def annots_get_set(self, obj: Optional[Any] = None) -> Set[str]:
        """get undefined annotated attributes in class (not instance!)
        """
        annots = set()
        if obj is None:
            obj = self
        mro = obj.__class__.__mro__
        for cls in mro[:-1]:
            if cls == tuple and hasattr(obj, "_fields"):    # NamedTuple
                return set(obj._fields).difference(set(obj._field_defaults))
            if not hasattr(cls, "__annotations__"):     # for last class (tuple) in NamedTuple!
                continue
            for name in set(cls.__annotations__):
                if not hasattr(cls, name):
                    annots.update({name, })
        # print(annots)
        return annots

    def annots_get_dict(self, obj: Optional[Any] = None) -> Union[Dict[str, Any], NoReturn]:
        """get dict of undefined annotated attributes in class but defined in instance!
        """
        annots = dict()
        for name in self.annots_get_set(obj):
            annots.update({name: self.attr_get_case_insensitive(name, obj)})
        return annots

    def annots_get_values(self, obj: Optional[Any] = None) -> Union[Iterable[Any], NoReturn]:
        """get iterable values of undefined annotated attributes in class but defined in instance!
        """
        return self.annots_get_dict(obj).values()

    def attr_get_case_insensitive(self, name: str, obj: Optional[Any] = None) -> Union[str, NoReturn]:
        """get value for attr name without case sense.
        if no attr name in source - raise!
        """
        if obj is None:
            obj = self

        attrs_all = list(filter(lambda attr: not callable(getattr(obj, attr)) and not attr.startswith("__"), dir(obj)))

        attrs_similar = list(filter(lambda attr: attr.lower() == name.lower(), attrs_all))
        if len(attrs_similar) == 1:
            return getattr(obj, attrs_similar[0])
        elif len(attrs_similar) == 0:
            msg = f"[CRITICAL]no[{name=}] in any cases [{attrs_all=}]"
            raise Exx_AttrNotExist(msg)
        else:
            msg = f"[CRITICAL]exists several similar [{attrs_similar=}]"
            raise Exx_AttrNotExist(msg)

    def annots_check_values_exists(self, obj: Optional[Any] = None) -> Union[bool, NoReturn]:
        """check all annotations have values!
        Raise if not any value
        """
        self.annots_get_dict(obj)
        return True


# =====================================================================================================================
