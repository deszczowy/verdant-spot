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
    
    @pyqtSlot()
    def refresh_data(self) -> None:
        print("refresh")
        self.renderer.render()
        self.signal_show_project_render.emit(self.renderer.get())

    @pyqtSlot(str)
    def store_project(self, project_file_path: str) -> None:
        print(project_file_path)
        if self.project_file != "":
            #opened
            if self.project_file != project_file_path:
                print("save as")
                VSaver().store(self.project_data, project_file_path)
                self.project_file = project_file_path
            else:
                print("regular save")
                VSaver().store(self.project_data, self.project_file)
        else:
            # new project
            if self.project_data is None:
                print("no project")
                self.signal_inform_user.emit("Open or create project")
            else:
                print("save new")
                VSaver().store(self.project_data, project_file_path)
                self.project_file = project_file_path