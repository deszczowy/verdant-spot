from .base import VBase

class VPoint(VBase):
    def __init__(self) -> None:
        super().__init__()
        self.X: float = None
        self.Y: float = None
    
    def from_data_string(self, data: str) -> None:
        p = data.split(",")
        try:
            self.X = float(p[0])
            self.Y = float(p[1])
        finally:
            if self.X is not None and self.Y is not None:
                self._set_valid()

    def from_data(self, x: float, y: float) -> None:
        self.X = x
        self.Y = y
        
        if self.X is not None and self.Y is not None:
            self._set_valid()

    def to_debug(self) -> str:
        return "({}, {})".format(self.X, self.Y)
