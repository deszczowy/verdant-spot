from .base import VBase

class VPoint(VBase):
    def __init__(self, x: float, y: float) -> None:
        super().__init__()
        self.X: float = x
        self.Y: float = y
        self._set_valid()
    
    def to_debug(self) -> str:
        return "({}, {})".format(self.X, self.Y)
