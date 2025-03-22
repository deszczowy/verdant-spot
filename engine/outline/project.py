from .base import VBase
from .layertype import VLayerType
from .kindtype import VKindType
from .info import VInfo
from .layer import VLayer
from .list import VList
from .object import VObject
from .point import VPoint

class VProject(VBase):
    layer_dictionary: VList[VLayerType] = VList()
    kind_dictionary: VList[VKindType] = VList()
    Info = VInfo()
    Layers: VList[VLayer] = VList()

    ### Dictionary entries

    def add_layer_type_entry_from_datastring(self, datastring: str) -> None:
        entry = VLayerType()
        entry.from_data_string(datastring)
        self.layer_dictionary.append(entry)

    def add_object_kind_entry_from_datastring(self, datastring: str) -> None:
        entry = VKindType()
        entry.from_data_string(datastring)
        self.kind_dictionary.append(entry)
    
    ### Layers

    def sort_layers_definitions(self) -> None:
        self.layer_dictionary.sort(key=lambda x: x.Position)

    ### Builders

    def rebuild_layers_from_dictionary(self) -> None:
        self.Layers = VList()

        for layer_definition in self.layer_dictionary:
            layer = VLayer()
            layer.from_data_string(layer_definition.Label)
            self.Layers.append(layer)
    
    def store_point_in_last_object_of_layer_based_on_datastring(self, layer_id: int, datastring: str) -> None:
        p = VPoint()
        p.from_data_string(datastring)
        self.Layers[layer_id].Objects[-1].Points.append(p)

    def store_object_in_layer_based_on_datastring(self, layer_id: int, datastring: str) -> None:
        o = VObject()
        o.from_data_string(datastring)
        self.Layers[layer_id].Objects.append(o)    

    ### Base class overload

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
