from outline import *

class VReader:

    def read(self, filename):

        self.data = ""
        self.project = None
        self.work = False

        with open(filename) as file:
            while l := file.readline():

                line = l.rstrip()

                if VTools.is_command(line):
                    print("Command: {} Data: {}".format(line, self.data))
                    self.process(line)
                else:
                    d = line
                    if self.data != "":
                        d = "\n" + d
                    self.data += d
                
                if not self.work:
                    break

    def process(self, cmd):
        match cmd:
            case VCommand.VerdantSpotStart: self.__start()
            case VCommand.NextLayer: self.__jump_to_next_layer()
            case VCommand.Name: self.__store_name()
            case VCommand.Desctiption: self.__store_description()
            case VCommand.Author: self.__store_author()
            case VCommand.BorderLeft: self.__store_border("L")
            case VCommand.BorderTop: self.__store_border("T")
            case VCommand.BorderRight: self.__store_border("R")
            case VCommand.BorderBottom: self.__store_border("B")
            case VCommand.LayerEntry: self.__store_layer_dictionary_entry()
            case VCommand.KindEntry: self.__store_object_kind_dictionary_entry()
            case VCommand.ProcessDictionaries: self.__process_dictionaries()
            case VCommand.Object: self.__store_object_in_current_layer()
            case VCommand.Point: self.__store_point_in_current_object()
            case VCommand.Stop: self.__stop()
    
    def __finalize_command(self) -> None:
        self.data = ""

    def __start(self) -> None:
        self.work = True
        self.project = VProject()
        self.layer_index = 0
        print("Start")

    def __stop(self) -> None:
        self.work = False

    def __jump_to_next_layer(self) -> None:
        self.layer_index += 1
        if self.layer_index >= len(self.project.Layers):
            print("EXCEPTION")
        self.__finalize_command()
    
    def __store_name(self) -> None:
        self.project.Info.Name = self.data
        self.__finalize_command()

    def __store_description(self) -> None:
        self.project.Info.Description = self.data
        self.__finalize_command()
    
    def __store_author(self) -> None:
        self.project.Info.Author = self.data
        self.__finalize_command()
    
    def __store_border(self, edge: str) -> None:
        try:
            value = float(self.data)
            match edge:
                case "L": self.project.Info.Border.Left = value
                case "R": self.project.Info.Border.Right = value
                case "T": self.project.Info.Border.Top = value
                case "B": self.project.Info.Border.Bottom = value
        finally:
            self.__finalize_command()
    
    def __store_layer_dictionary_entry(self) -> None:
        entry = VLayerType()
        entry.from_data_string(self.data)

        print(entry.to_debug())
        if entry.is_valid():
            self.project.layer_dictionary.append(entry)
        self.__finalize_command()

    def __store_object_kind_dictionary_entry(self) -> None:
        entry_data = self.data.split(":")
        try:
            symbol = entry_data[0]
            label = entry_data[1]

            self.project.kind_dictionary.append(VKindType(symbol, label))
        finally:
            self.__finalize_command()
    
    def __process_dictionaries(self) -> None:
        self.project.layer_dictionary.sort(key=lambda x: x.Position)
        self.project.Layers = []

        for layer_definition in self.project.layer_dictionary:
            self.project.Layers.append(VLayer(layer_definition.Label))

    def __store_object_in_current_layer(self) -> None:
        data = self.data.split(":")
        try:
            self.project.Layers[self.layer_index].Objects.append(VObject(data[1], data[0]))
        finally:
            self.__finalize_command()
            
    def __store_point_in_current_object(self)-> None:
        data = self.data.split(",")
        try:
            x = float(data[0])
            y = float(data[1])
            self.project.Layers[self.layer_index].Objects[-1].Points.append(VPoint(x,y))
        finally:
            self.__finalize_command()
    
    def print_debug(self) -> None:
        print(self.project.to_debug())

filename = ".exp/twelve/data.txt"
p = VReader()
p.read(filename)
p.print_debug()