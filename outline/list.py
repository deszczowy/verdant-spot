from .base import VBase
    
class VList(list):
    def __init__(self):
        super().__init__([])

    def __setitem__(self, index: int, item: VBase):
        if isinstance(item, VBase) and item.is_valid():
            super().__setitem__(index, item)

    def insert(self, index: int, item: VBase):
        if isinstance(item, VBase) and item.is_valid():
            super().insert(index, item)

    def append(self, item):
        if isinstance(item, VBase) and item.is_valid():
            super().append(item)

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            for item in other:
                if item.is_valid():
                    super().append(item)