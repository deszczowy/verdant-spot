from .base import VBase

class VObject(VBase):
    def __init__(self, label: str, kind: str) -> None:
        super().__init__()
        self.Label: str = label
        self.Kind: str = kind
        self.Points = []
        self._set_valid()
    
    def to_debug(self) -> str:
        d = "{} ({})".format(self.Label, self.Kind)
        for p in self.Points:
            d += "\n{}".format(p.to_debug())
        return d
