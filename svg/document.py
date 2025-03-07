from .templates import TEMPLATES
from .classes import CLASSESS
from .kind import Kind
from .base import SvgBaseObject
from .layer import SvgLayer

class SvgDocument(SvgBaseObject):

    def __init__(self) -> None:
        super().__init__(0, Kind.Document)
        self.layers = []
    
    def setup(self, document_info: dict) -> None:
        self.project_name = document_info["name"]
        self.description = document_info["description"]
        self.author = document_info["author"]

        self.right = float(document_info["border_right"])
        self.left = float(document_info["border_left"])
        self.top = float(document_info["border_top"]) 
        self.bottom = float(document_info["border_bottom"])

        self.width = self.right - self.left
        self.height = self.top - self.bottom
    
    def add_layer(self, layer: SvgLayer) -> None:
        self.layers.append(layer)
    
    def put_on_last_layer(self, element: SvgBaseObject) -> None:
        self.layers[-1].put(element)

    def render(self, content: str) -> str:
        s = self._get_styles()
        return TEMPLATES["DOCUMENT"].format(
            w=self.width, 
            h=self.height, 
            x0=self.left, 
            y0=self.bottom, 
            x1=self.right,
            y1=self.top,
            styles=s, 
            id=self.identifier, 
            content=self.content
        )
    
    def _get_styles(self) -> str:
        s = ""
        for c in CLASSESS:
            s += c
        return s