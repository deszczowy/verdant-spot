from .base import VBase

class VKindType(VBase):
    def __init__(self, symbol: str, label: str) -> None:
        super().__init__()
        self.Symbol = symbol
        self.Label = label
        self._set_valid()
    
    def to_debug(self) -> str:
        return "Kind definition: {}, symbol {}".format(self.Label, self.Symbol)
