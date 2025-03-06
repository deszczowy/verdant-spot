from .layer import SvgLayer
from .path import SvgPath
from .base import SvgBaseObject

class ProjectRenderer:

    def __init__(self):
        # gathering data
        self.layer = 0
        self.element = 0
        self.path = []
        self.current = None

        # structure of data
        self.layers = []

        # results
        self.rendered_svg = ""
    
    def render(self, data: list[dict]) -> str:
        #print(data)
        for e in data:
            self.current = e
            self._new_layer()
            self._new_element()
        self._build_last()

        for l in self.layers:
            self.rendered_svg += l.render()
        return self.rendered_svg

    def _new_layer(self) -> None:
        id = self.current["layer_id"]
        if id > self.layer:
            self.layer = id
            self.layers.append(SvgLayer(id))

    def _new_element(self) -> None:
        if self.current["id"] != self.element:
            self._build_last()
            self._gather()
        else:
            self._update(element)

    def _gather(self) -> None:
        self.path = [self._collect_point()]
        self.element = self.current["id"]

    def _update(self, element: dict) -> None:
        self.path.append(self._collect_point())
    
    def _collect_point(self) -> (float, float):
        x = self.current["x"]
        y = self.current["y"]
        return (x, y)

    def _build_last(self):
        if self.element > 0:
            e = self._build()
            self.layers[-1].put(e)
    
    def _build(self) -> SvgBaseObject:
        match self.current["kind"]:
            case "TR" | "SH": return SvgPath(self.current["id"], self.current["kind"], self.path)