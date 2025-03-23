from .templates import TEMPLATES
from .kind import Kind
from .base import SvgBaseObject
from .circle import SvgCircle
from outline import VLayer, VObject

class SvgLayer(SvgBaseObject):

    def __init__(self):
        super().__init__(Kind.Layer)
        self.circle_renderer = SvgCircle()

    def render(self, layer_data: VLayer) -> str:
        c = self.__get_content(layer_data)
        return TEMPLATES["LAYER"].format(layer_id=layer_data.id(), content=c)
    
    def __get_content(self, layer_data: VLayer) -> str:
        rc = ""
        for o in layer_data.Objects:
            rc += self.__get_object(o)
        return rc
    
    def __get_object(self, object_data: VObject) -> str:
        match object_data.Kind:
            case "TR" | "SH": return self.circle_renderer.render(object_data)
            #case "GR" | "BD" | "SC": return SvgPath(self.current["id"], self.current["kind"], self.path)
            case _: return "NOT IMPLEMENTED"