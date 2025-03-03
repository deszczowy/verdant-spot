from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class Panel(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addSpacing(0)
        self.setLayout(self.layout)
        self.setAutoFillBackground(True)

    def set_color(self, color):
        if color == None:
            color = QtWhite

        p = self.palette()
        p.setColor(self.backgroundRole(), color)
        self.setPalette(p)