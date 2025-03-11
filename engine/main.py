from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from db import ProjectDb

class VerdantEngine(QObject):

    signal_project_title_updated = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.project_file = ""
        self.project_db = None
        self.project_info = {}
    
    @pyqtSlot(str)
    def load_project(self, project_file_path: str) -> None:
        self.project_db = ProjectDb(project_file_path)
        self.project_info = self.project_db.get_info()

        self.signal_project_title_updated.emit(self.project_info["name"])
