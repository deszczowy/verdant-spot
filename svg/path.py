from .templates import TEMPLATES
from .kind import Kind
from .base import SvgBaseObject

class SvgPath(SvgBaseObject):

    def __init__(self, id: int, style_class: str, points: list[(float, float)]) -> str:
        super().__init__(id, Kind.Element)
        self.style_class = style_class
        self.points = points

    def render(self) -> str:
        d = self._get_path_d()
        return TEMPLATES["path"].format(element_id=self.identifier, d=d, style=self.style_class)

    def _get_path_d(self):
        if len(self.points) == 0:
            return ""
        
        d = ""
        c = "M"
        for p in self.points:
            d += "{command}{px:.2f} {py:.2f} ".format(command=c, px=p[0], py=p[1])
            c = "L"
        
        d += "Z"
        return d
