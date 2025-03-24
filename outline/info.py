from .base import VBase
from .point import VPoint

class VInfo(VBase):

    def __init__(self) -> None:
        super().__init__()
        self.set_id(0)
        
        self.Name: str = ""
        self.Description: str = ""
        self.Author: str = ""
        self.Size: VPoint = VPoint()
        self._set_valid()
    
    def store_map_size_from_datastring(self, datastring: str) -> None:
        self.Size.from_data_string(datastring)
    
    def to_debug(self) -> str:
        return "Project\nName: {}\nAuthor: {}\nDescription:\n{}\nSize: {}".format(
            self.Name, self.Author, self.Description, self.Size.to_debug())
