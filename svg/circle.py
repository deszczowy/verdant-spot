from .templates import TEMPLATES
from .kind import Kind
from .base import SvgBaseObject
from .coordinate import SvgCoordinate
from outline import VObject

class SvgCircle(SvgBaseObject):

    def __init__(self) -> None:
        super().__init__(Kind.Element)

    def render(self, object_data: VObject, coord: SvgCoordinate) -> str:
        if len(object_data.Points) == 0:
            return ""

        p = object_data.Points[0]
        (ax, ay) = coord.get_svg_point(p.X, p.Y)

        return TEMPLATES["CIRCLE"].format(
            element_id=object_data.id(),
            px=ax,
            py=ay,
            radius=self.__calculate_radius(object_data.Kind),
            caption=object_data.Label)

    def __calculate_radius(self, circle_kind: str):
        match circle_kind:
            case "SH":
                r = 25
            case "TR":
                r = 50
            case _:
                r = 0
        return r