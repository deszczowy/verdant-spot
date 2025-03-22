from .base import VBase

class VObject(VBase):
    def __init__(self) -> None:
        super().__init__()
        self.Label: str = ""
        self.Kind: str = ""
        self.Points = []

    def from_data_string(self, data: str) -> None:
        o = data.split(":")
        try:
            self.Kind = o[0]
            self.Label = o[1]
        finally:
            if self.Kind != "" and self.Label != "":
                self._set_valid()

    def from_data(self, label: str, kind: str) -> None:
        self.Label = label
        self.Kind = kind
        if self.Kind != "" and self.Label != "":
            self._set_valid()
    
    def to_debug(self) -> str:
        d = "{} ({})".format(self.Label, self.Kind)
        for p in self.Points:
            d += "\n{}".format(p.to_debug())
        return d
