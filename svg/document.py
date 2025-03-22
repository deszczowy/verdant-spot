from .templates import TEMPLATES
from .classes import CLASSES
from .kind import Kind
from .base import SvgBaseObject
from outline import VProject

class SvgDocument(SvgBaseObject):

    def __init__(self) -> None:
        super().__init__(Kind.Document)
    
    def render(self, project_data: VProject) -> str:
        w = project_data.Info.Border.Right - project_data.Info.Border.Left
        h = project_data.Info.Border.Top - project_data.Info.Border.Bottom
        s = self._get_styles()
        return TEMPLATES["DOCUMENT"].format(
            w=w, 
            h=h, 
            x0=project_data.Info.Border.Left, 
            y0=project_data.Info.Border.Bottom, 
            x1=project_data.Info.Border.Right,
            y1=project_data.Info.Border.Top,
            styles=s, 
            id=self.identifier(project_data.id())
        )
    
    def _get_styles(self) -> str:
        s = ""
        for c in CLASSES:
            s += CLASSES[c]
        return s