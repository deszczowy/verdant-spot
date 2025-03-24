from .kind import Kind

class SvgBaseObject:

    def __init__(self, kind: Kind):
        self.kind = kind

    def identifier(self, id) -> str:
        prefix = "U"
        if self.kind == Kind.Layer:
            prefix = "L"
        elif self.kind == Kind.Element:
            prefix = "E"
        elif self.kind == Kind.Document:
            prefix = "D"
        
        return "{p}{i}".format(p=prefix, i=id)