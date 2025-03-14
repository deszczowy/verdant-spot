from .base import VBase
from .area import VArea

class VInfo(VBase):
    Name: str = ""
    Description: str = ""
    Author: str = ""
    Border: VArea = VArea()

    def __init__(self) -> None:
        super().__init__()
        self._set_valid()
    
    def to_debug(self) -> str:
        return "Project\nName: {}\nAuthor: {}\nDescription:\n{}\nBorder: {}".format(
            self.Name, self.Author, self.Description, self.Border.to_debug())
