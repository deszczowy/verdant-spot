from .base import VBase
from .layertype import VLayerType
from .kindtype import VKindType
from .info import VInfo
from .layer import VLayer

class VProject(VBase):
    layer_dictionary: list[VLayerType] = []
    kind_dictionary: list[VKindType] = []
    Info = VInfo()
    Layers: list[VLayer] = []

    def to_debug(self) -> str:
        i = self.Info.to_debug()
        
        x = y = ""
        for l in self.layer_dictionary:
            x += "\n" + l.to_debug()
        for k in self.kind_dictionary:
            y += "\n" + k.to_debug()
        d = "Layers:{}\nKinds:{}".format(x, y)

        l = "Layers/Objects:"
        for x in self.Layers:
            l += "\n" + x.to_debug()
        
        return "{}\n{}\n{}".format(i, d, l)
