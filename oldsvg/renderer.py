from .document import SvgDocument

class ProjectRenderer:
    
    def render(self, document: SvgDocument) -> str:
        content = ""
        for layer in document.layers:
            content += layer.render()
        return document.render(content)