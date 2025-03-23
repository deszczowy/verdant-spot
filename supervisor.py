from view import VMainView
from engine import VEngine

class Supervisor:

    def __init__(self) -> None:
        self.view = VMainView()
        self.engine = VEngine()
        self.__connect()
    
    def run(self) -> None:
        self.view.show()

    def __connect(self) -> None:
        # Engine signals
        self.engine.signal_project_title_updated.connect(self.view.update_title)
        self.engine.signal_show_project_render.connect(self.view.update_preview)

        # View signals
        self.view.project_opened.connect(self.engine.load_project)