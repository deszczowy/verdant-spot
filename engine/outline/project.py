from .base import VBase
from .layertype import VLayerType
from .kindtype import VKindType
from .info import VInfo
from .layer import VLayer
from .list import VList

class VProject(VBase):
    layer_dictionary: VList[VLayerType] = VList()
    kind_dictionary: VList[VKindType] = VList()
    Info = VInfo()
    Layers: VList[VLayer] = VList()

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
