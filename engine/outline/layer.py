from .base import VBase
from .list import VList
from .object import VObject

class VLayer(VBase):

    def __init__(self):
        super().__init__()
        self.Label = ""
        self.Objects: VList[VObject] = []
    
    def from_data_string(self, data: str) -> None:
        self.Label = data.strip()
        if self.Label != "":
            self._set_valid()

    def from_data(self, label: str) -> None:
        self.Label = label.strip()
        if self.Label != "":
            self._set_valid()

    def to_debug(self) -> str:
        od = ""
        for o in self.Objects:
            od += "\n{}".format(o.to_debug())
        return "{} ({}) id: {}\nObjects:{}".format(self.Label, len(self.Objects), self.id(), od)
