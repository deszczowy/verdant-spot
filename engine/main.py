from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from .reader import VReader
from .saver import VSaver
from .renderer import VRenderer
from .model import VModel

class VEngine(QObject):

    signal_project_title_updated = pyqtSignal(str)
    signal_show_project_render = pyqtSignal(str)
    signal_connect_data_model = pyqtSignal(VModel)

    def __init__(self) -> None:
        super().__init__()
        self.project_file = ""
        self.project_data = None
        self.project_model = None
        self.reader = VReader()
        self.renderer = VRenderer()
    
    @pyqtSlot(str)
    def load_project(self, project_file_path: str) -> None:
        self.project_file = project_file_path
        self.project_data = self.reader.read(self.project_file)
        self.project_model = VModel(self.project_data)
        self.reader.print_debug()
        self.renderer.connect(self.project_data)
        
        self.signal_project_title_updated.emit(self.project_data.Info.Name)
        self.signal_show_project_render.emit(self.renderer.get())
        self.signal_connect_data_model.emit(self.project_model)

    @pyqtSlot(str)
    def store_project(self, project_file_path: str) -> None:
        VSaver().store(self.project_data, project_file_path)