from .templates import TEMPLATES
from .classes import CLASSES
from .kind import Kind
from .base import SvgBaseObject
from outline import VProject

class SvgDocument(SvgBaseObject):

    def __init__(self) -> None:
        super().__init__(Kind.Document)
    
    def render(self, project_data: VProject) -> str:
        s = self._get_styles()
        return TEMPLATES["DOCUMENT"].format(
            w=project_data.Info.Size.X, 
            h=project_data.Info.Size.Y,
            x0=0, 
            y0=0, 
            x1=project_data.Info.Size.X,
            y1=project_data.Info.Size.Y,
            styles=s, 
            id=self.identifier(project_data.id())
        )
    
    def _get_styles(self) -> str:
        s = ""
        for c in CLASSES:
            s += CLASSES[c]
        return s