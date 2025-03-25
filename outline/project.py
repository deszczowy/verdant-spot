from .base import VBase
from .layertype import VLayerType
from .kindtype import VKindType
from .info import VInfo
from .layer import VLayer
from .list import VList
from .object import VObject
from .point import VPoint

class VProject(VBase):
    LayersDefinitions: VList[VLayerType] = VList()
    KindsDefinitions: VList[VKindType] = VList()
    Info = VInfo()
    Layers: VList[VLayer] = VList()
    __counter: int = 0

    ### Dictionary entries

    def add_layer_type_entry_from_datastring(self, datastring: str) -> None:
        entry = VLayerType()
        entry.from_data_string(datastring)
        self.LayersDefinitions.append(entry)

    def add_object_kind_entry_from_datastring(self, datastring: str) -> None:
        entry = VKindType()
        entry.from_data_string(datastring)
        self.KindsDefinitions.append(entry)
    
    ### Layers

    def sort_layers_definitions(self) -> None:
        self.LayersDefinitions.sort(key=lambda x: x.Position)

    ### Builders

    def rebuild_layers_from_dictionary(self) -> None:
        self.Layers = VList()

        for layer_definition in self.LayersDefinitions:
            layer = VLayer()
            layer.set_id(self.new_id())
            layer.from_data_string(layer_definition.Label)
            self.Layers.append(layer)
    
    def store_point_in_last_object_of_layer_based_on_datastring(self, layer_id: int, datastring: str) -> None:
        if layer_id == -1:
            return

        p = VPoint()
        p.from_data_string(datastring)
        self.Layers[layer_id].Objects[-1].Points.append(p)

    def store_object_in_layer_based_on_datastring(self, layer_id: int, datastring: str) -> None:
        if layer_id == -1:
            return

        o = VObject()
        o.set_id(self.new_id())
        o.from_data_string(datastring)
        self.Layers[layer_id].Objects.append(o)    

    ### Maintenance

    def new_id(self) -> int:
        self.__counter += 1
        return self.__counter

    ### Base class overload

    def to_debug(self) -> str:
        i = self.Info.to_debug()
        
        x = y = ""
        for l in self.LayersDefinitions:
            x += "\n" + l.to_debug()
        for k in self.KindsDefinitions:
            y += "\n" + k.to_debug()
        d = "Layers:{}\nKinds:{}".format(x, y)

        l = "Layers/Objects:"
        for x in self.Layers:
            l += "\n" + x.to_debug()
        
        return "{}\n{}\n{}".format(i, d, l)
