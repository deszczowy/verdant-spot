from .templates import TEMPLATES
from .kind import Kind
from .base import SvgBaseObject

class SvgCircle(SvgBaseObject):

    def __init__(self, id: int, circle_kind: str, caption: str, points: list[(float, float)]) -> str:
        super().__init__(id, Kind.Element)
        self.points = points
        self.caption = caption
        self._calculate_diameter(circle_kind)

    def render(self) -> str:
        if len(self.points) == 0:
            return ""
        p = self.points[0]
        return TEMPLATES["CIRCLE"].format(element_id=self.identifier, px=p[0], py=p[1], diameter=self.diameter, caption=self.caption)

    def _calculate_diameter(self, circle_kind: str):
        match circle_kind:
            case "SH":
                d = 50
            case "TR":
                d = 50
            case _:
                d = 0
        self.diameter = d