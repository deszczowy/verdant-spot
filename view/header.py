from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt

from .tools import *

class VHeader(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(50)

        #self.setStyleSheet("border-bottom: 1px solid #fafafa;")

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
        
        self.status_label = QLabel("Status")
        self.status_label.setAlignment(Qt.AlignRight)
        self.layout = QHBoxLayout(self)
        
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.__build_toolbar()
    
    def __build_toolbar(self) -> None:
        #self.layout.addStretch()
        self.data_button = create_toolbar_button("+")
        self.layout.addWidget(self.status_label)
        self.layout.addWidget(self.data_button)