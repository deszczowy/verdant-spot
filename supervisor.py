from view import VerdantMainView
from engine import VerdantEngine

class Supervisor:

    def __init__(self) -> None:
        self.view = VerdantMainView()
        self.engine = VerdantEngine()
        self.__connect()
    
    def run(self) -> None:
        self.view.show()

    def __connect(self) -> None:
        # Engine signals
        self.engine.signal_project_title_updated.connect(self.view.update_title)

        # View signals
        self.view.project_opened.connect(self.engine.load_project)