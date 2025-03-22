from .layer import SvgLayer
from .path import SvgPath
from .circle import SvgCircle
from .document import SvgDocument
from .base import SvgBaseObject

class ProjectBuilder:

    def __init__(self):
        # gathering data
        self.layer = 0
        self.element = 0
        self.path = []
        self.current = None

        # structure of data
        self.document = SvgDocument()
    
    def build(self, info: dict, data: list[dict]) -> SvgDocument:
        self.document.setup(info)
        for e in data:
            self.current = e
            self._new_layer()
            self._new_element()
        self._build_last()
        return self.document

    def _new_layer(self) -> None:
        id = self.current["layer_id"]
        if id > self.layer:
            self.layer = id
            self.document.add_layer(SvgLayer(id))

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
            self.document.put_on_last_layer(e)
    
    def _build(self) -> SvgBaseObject:
        match self.current["kind"]:
            case "TR" | "SH": return SvgCircle(self.current["id"], self.current["kind"], self.current["caption"], self.path)
            case "GR" | "BD" | "SC": return SvgPath(self.current["id"], self.current["kind"], self.path)