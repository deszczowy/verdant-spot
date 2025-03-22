from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from .reader import VReader

from svg import SvgDocument

class VEngine(QObject):

    signal_project_title_updated = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.project_file = ""
        self.project_data = None
    
    @pyqtSlot(str)
    def load_project(self, project_file_path: str) -> None:
        self.project_file = project_file_path
        r = VReader()
        self.project_data = r.read(self.project_file)
        r.print_debug()

        svg = SvgDocument()
        print(svg.render(self.project_data))

        self.signal_project_title_updated.emit(self.project_data.Info.Name)
