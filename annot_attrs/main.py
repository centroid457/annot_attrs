from typing import *


# =====================================================================================================================
class AnnotAttrs:
    def annots_set(self) -> Set[str]:
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


# =====================================================================================================================
