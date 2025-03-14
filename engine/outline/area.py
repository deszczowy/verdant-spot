from .base import VBase

class VArea(VBase):
    Left: float = 0.0
    Right: float = 0.0
    Top: float = 0.0
    Bottom: float = 0.0

    def __init__(self) -> None:
        super().__init__()
        self._set_valid()
    
    def to_debug(self) -> str:
        return "Area:\n    {}\n{}   {}\n    {}".format(
            self.Top, self.Left, self.Right, self.Bottom)