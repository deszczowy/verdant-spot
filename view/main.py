import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from .preview import MapPreview

from .menu import VMainMenu
from .header import VHeader

class VMainView(QMainWindow):

    project_opened = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("VerdantSpot")
        self.setGeometry(100, 100, 800, 600)
        self._build_ui()
    
    def _build_ui(self):
        # Główny widget centralny z layoutem
        self.window_container = QWidget()
        self.setCentralWidget(self.window_container)
        self.main_layout = QHBoxLayout(self.window_container)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        self._build_menu()
        self._stack_ui()

    def _build_menu(self):

        # Menu boczne
        self.menu_widget = VMainMenu(parent=self.window_container)
        self.menu_widget.reposition()
        self.menu_widget.new_btn.clicked.connect(self.btn_click)
        


        # Kontener dla Main i Status
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # Pasek statusu
        self.status_bar = VHeader()
        
        
        

        # Główny obszar
        self.main_area = MapPreview()

        # Dodanie Status i Main do content_layout
        self.content_layout.addWidget(self.status_bar)
        self.content_layout.addWidget(self.main_area)

    def _stack_ui(self):
        # Dodanie widgetów do głównego layoutu
        #self.main_layout.addWidget(self.menu_widget)
        self.main_layout.addWidget(self.content_widget)
        # Timer do sprawdzania pozycji myszy
        

        # Włączanie śledzenia myszy
        self.setMouseTracking(True)
        



    def resizeEvent(self, event):
        #self.menu_widget.setFixedHeight(self.height())
        self.menu_widget.reposition()
        super().resizeEvent(event)
    
    def btn_click(self) -> None:
        name = "dev/data.txt"
        self.project_opened.emit(name)
    
    @pyqtSlot(str)
    def update_title(self, new_title: str = None) -> None:
        caption = "Verdant Spot"
        if new_title != None:
            caption += ": {}".format(new_title)
        self.setWindowTitle(caption)
    
    @pyqtSlot(str)
    def update_preview(self, svg_data: str) -> None:
        map = bytearray(svg_data, encoding='utf-8')
        self.main_area.load(map)
