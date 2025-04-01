from outline import VProject, VLayer
from svg import SvgDocument, SvgLayer, SvgCoordinate, SvgGrid

class VRenderer:

    def __init__(self):
        self.project: VProject = None
        self.document: str = ""
        self.layers: dict = {}
        self.coordinate: SvgCoordinate = SvgCoordinate()
    
    def connect(self, project: VProject) -> None:
        self.layers = {}
        self.project = project
        self.render()
    
    def update(self) -> None:
        self.coordinate.up_to_date_with_project(self.project)
    
    def render(self) -> None:
        self.update()
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
        if layer.IsVirtual:
            svg = SvgGrid()
            self.layers[layer.id()] = svg.generate(
                width=self.project.Info.Size.X,
                height=self.project.Info.Size.Y,
                center_x=0.00,
                center_y=0.00,
                grid_spacing=50,
                coordinate_system=self.coordinate
            )
            print("virt")
        else:
            svg = SvgLayer()
            self.layers[layer.id()] = svg.render(layer, self.coordinate)
        
