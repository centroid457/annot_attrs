from typing import *


# =====================================================================================================================
class Exx_AttrNotExist(Exception):
    pass


# =====================================================================================================================
class AnnotAttrs:
    """
    DONT USE with typing.NamedTuple! will raise!
    """
    def __getattr__(self, item: str) -> Union[str, NoReturn]:
        if item in ["__isabstractmethod__", ]:
            return
        else:
            return self.attr_get_case_insensitive(item)

    def __getitem__(self, key: str) -> Union[str, NoReturn]:
        return self.attr_get_case_insensitive(key)

    def __str__(self):
        result = "AnnotAttrs:"
        data = self.annots_get_dict()
        if data:
            for key, value in data.items():
                result += f"\n{key}={value}"
        else:
            result += f"\ndata=None"
        return result

    def print(self) -> None:
        print(self)

    def annots_get_set(self) -> Set[str]:
        """
        :return: set of undefined annotated attributes in class (not instance!)
        """
        annots = set()
        for cls in self.__class__.__mro__[:-1]:
            for name in set(cls.__annotations__):
                if not hasattr(cls, name):
                    annots.update({name, })
        # print(annots)
        return annots

    def annots_get_dict(self) -> Union[Dict[str, Any], NoReturn]:
        """
        :return: dict of undefined annotated attributes in class but defined in instance!
        """
        annots = dict()
        for name in self.annots_get_set():
            annots.update({name: self.attr_get_case_insensitive(name)})
        return annots

    def attr_get_case_insensitive(self, name: str) -> Union[str, NoReturn]:
        """
        get value for attr name without case sense.
        if no attr name in source - raise!
        """
        attrs_all = list(filter(lambda attr: not callable(getattr(self, attr)) and not attr.startswith("__"), dir(self)))

        attrs_similar = list(filter(lambda attr: attr.lower() == name.lower(), attrs_all))
        if len(attrs_similar) == 1:
            return getattr(self, attrs_similar[0])
        elif len(attrs_similar) == 0:
            msg = f"[CRITICAL]no[{name=}] in any cases [{attrs_all=}]"
            raise Exx_AttrNotExist(msg)
        else:
            msg = f"[CRITICAL]exists several similar [{attrs_similar=}]"
            raise Exx_AttrNotExist(msg)

    def annots_check_values_exists(self) -> Union[True, NoReturn]:
        """
        check all annotations have values!
        Raise if not any value
        """
        self.annots_get_dict()
        return True


# =====================================================================================================================
