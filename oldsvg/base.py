from .kind import Kind

class SvgBaseObject:

    def __init__(self, id: int, kind: Kind):
        self.id = id
        self.kind = kind
        self._identifier()

    def _identifier(self) -> str:
        prefix = "U"
        if self.kind == Kind.Layer:
            prefix = "L"
        elif self.kind == Kind.Element:
            prefix = "E"
        elif self.kind == Kind.Document:
            prefix = "D"
        
        self.identifier = "{p}{i}".format(p=prefix, i=self.id)