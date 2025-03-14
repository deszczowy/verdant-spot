from .base import VBase
from .object import VObject

class VLayer(VBase):
    def __init__(self, label: str) -> None:
        super().__init__()
        self.Label: str = label
        self.Objects: list[VObject] = []
        self._set_valid()
    
    def to_debug(self) -> str:
        od = ""
        for o in self.Objects:
            od += "\n{}".format(o.to_debug())
        return "{} ({})\nObjects:{}".format(self.Label, len(self.Objects), od)
