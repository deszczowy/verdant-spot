from .templates import TEMPLATES
from .kind import Kind
from .base import SvgBaseObject
from outline import VLayer

class SvgLayer(SvgBaseObject):

    def __init__(self):
        super().__init__(Kind.Layer)

    def render(self, layer_data: VLayer) -> str:
        c = self.__get_content(layer_data)
        return TEMPLATES["LAYER"].format(layer_id=layer_data.id(), content=c)
    
    def __get_content(self, layer_data: VLayer) -> str:
        rc = ""
        for o in layer_data.Objects:
            rc += "{}({}) ".format(o.Label, o.Kind)
        return rc