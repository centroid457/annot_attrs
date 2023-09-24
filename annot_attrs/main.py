from typing import *


# =====================================================================================================================
class AnnotAttrs:
    def annots_list(self) -> List[str]:
        annots = set()
        for cls in self.__class__.__mro__[:-1]:
            for name in set(cls.__annotations__):
                if not hasattr(cls, name):
                    annots.update({name, })
        annots = list(annots)
        # print(annots)
        return annots


# =====================================================================================================================
