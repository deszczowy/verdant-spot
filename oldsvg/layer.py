from .templates import TEMPLATES
from .kind import Kind
from .base import SvgBaseObject

class SvgLayer(SvgBaseObject):

    def __init__(self, id: int):
        super().__init__(id, Kind.Layer)
        self.elements = []

    def render(self) -> str:
        c = self._get_content()
        return TEMPLATES["LAYER"].format(layer_id=self.identifier, content=c)
    
    def put(self, element: SvgBaseObject) -> None:
        self.elements.append(element)
    
    def _get_content(self) -> str:
        rc = ""
        for e in self.elements:
            rc += e.render()
        return rc