from outline import VProject, VLayer
from svg import SvgDocument, SvgLayer

class VRenderer:

    def __init__(self):
        self.project: VProject = None
        self.document: str = ""
        self.layers: dict = {}
    
    def connect(self, project: VProject) -> None:
        self.layers = {}
        self.project = project
        self.render()
    
    def render(self) -> None:
        self.render_document()
        for l in self.project.Layers:
            self.render_layer(l)
    
    def get(self) -> str:
        d = ""
        for l in self.layers:
            d += self.layers[l]
        return "{}{}</svg>".format(self.document, d)
    
    def render_document(self) -> None:
        svg = SvgDocument()
        self.document = svg.render(self.project)
    
    def render_layer(self, layer):
        svg = SvgLayer()
        self.layers[layer.id()] = svg.render(layer)
        
