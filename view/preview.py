from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt

from .panel import Panel
import svg

class MapPreview(Panel):

    def __init__(self):
        super().__init__()
        super().set_color(Qt.white)

        map = svg.empty()
        self.svg = QSvgWidget()
        self.svg.setStyleSheet("background-color:white;")
        self.svg.renderer().load(map)
        self.svg.renderer().setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        self.layout.addWidget(self.svg)
    
    def load(self, data):
        self.svg.renderer().load(data)
        self.svg.renderer().setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
