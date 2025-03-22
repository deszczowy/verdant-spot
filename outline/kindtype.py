from .base import VBase

class VKindType(VBase):

    Symbol: str
    Label: str

    def from_data_string(self, data: str) -> None:
        bits = data.split(":")
        try:
            self.Symbol = bits[0]
            self.Label = bits[1]
        finally:
            self._set_valid()

    def from_data(self, symbol: str, label: str) -> None:
        self.Symbol = symbol
        self.Label = label
        self._set_valid()
    
    def to_debug(self) -> str:
        return "Kind definition: {}, symbol {}".format(self.Label, self.Symbol)
    
    def to_store(self) -> str:
        return "{}:{}".format(self.Symbol, self.Label)
