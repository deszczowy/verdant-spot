from .templates import TEMPLATES
from .kind import Kind
from .base import SvgBaseObject
from outline import VObject

class SvgPath(SvgBaseObject):

    def __init__(self) -> str:
        super().__init__(Kind.Element)

    def render(self, object_data: VObject) -> str:
        d = self._get_path_d(object_data)
        return TEMPLATES["PATH"].format(element_id=object_data.id(), d=d)

    def _get_path_d(self, object_data: VObject) -> str:
        if len(object_data.Points) == 0:
            return ""
        
        d = ""
        c = "M"
        for p in object_data.Points:
            d += "{command}{px:.2f} {py:.2f} ".format(command=c, px=p.X, py=p.Y)
            c = "L"
        
        d += "Z"
        return d
