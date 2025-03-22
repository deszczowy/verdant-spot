from .base import VBase

class VLayerType(VBase):

    Position: int
    Is_Visible: bool
    Label: str

    def from_data_string(self, data: str) -> None:
        bits = data.split(":")
        try:
            self.Position = int(bits[0])
            self.Is_Visible = self._is_true(bits[1])
            self.Label = bits[2]
        finally:
            self._set_valid()

    def from_data(self, position: int, is_visible: bool, label: str) -> None:
        self.Position = position
        self.Is_Visible = is_visible
        self.Label = label
        self._set_valid()
    
    def to_debug(self) -> str:
        return "Layer definition: {}, position {}, visible={}".format(self.Label, self.Position, self.Is_Visible)
    
    def to_store(self) -> str:
        v = "T" if self.Is_Visible else "N"
        return "{}:{}:{}".format(self.Position, v, self.Label)
