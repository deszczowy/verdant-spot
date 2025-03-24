from .templates import TEMPLATES
from .kind import Kind
from .base import SvgBaseObject
from .coordinate import SvgCoordinate
from outline import VObject

class SvgPath(SvgBaseObject):

    def __init__(self) -> str:
        super().__init__(Kind.Element)
        self.coordinate_system = None

    def render(self, object_data: VObject, coordinate_system: SvgCoordinate) -> str:
        self.coordinate_system = coordinate_system
        d = self._get_path_d(object_data)
        return TEMPLATES["PATH"].format(element_id=object_data.id(), d=d)

    def _get_path_d(self, object_data: VObject) -> str:
        if len(object_data.Points) == 0:
            return ""
        
        d = ""
        c = "M"
        for p in object_data.Points:
            (ax, ay) = self.coordinate_system.get_svg_point(p.X, p.Y)
            d += "{command}{px:.2f} {py:.2f} ".format(command=c, px=ax, py=ay)
            c = "L"
        
        d += "Z"
        return d
