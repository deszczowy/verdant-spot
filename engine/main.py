from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from .reader import VReader
from .saver import VSaver
from .renderer import VRenderer

class VEngine(QObject):

    signal_project_title_updated = pyqtSignal(str)
    signal_show_project_render = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.project_file = ""
        self.project_data = None
        self.reader = VReader()
        self.renderer = VRenderer()
    
    @pyqtSlot(str)
    def load_project(self, project_file_path: str) -> None:
        self.project_file = project_file_path
        self.project_data = self.reader.read(self.project_file)
        self.renderer.connect(self.project_data)
        
        self.signal_project_title_updated.emit(self.project_data.Info.Name)
        self.signal_show_project_render.emit(self.renderer.get())

    @pyqtSlot(str)
    def store_project(self, project_file_path: str) -> None:
        VSaver()