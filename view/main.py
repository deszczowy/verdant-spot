import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import pyqtSignal, pyqtSlot


from .preview import MapPreview

class VerdantMainView(QMainWindow):

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
        self.menu_widget = QWidget()
        self.menu_widget.setMinimumWidth(40)
        self.menu_widget.setMaximumWidth(40)  # Początkowa szerokość
        self.menu_widget.setStyleSheet("background-color: red;")

        # Przyciski w menu
        menu_layout = QVBoxLayout(self.menu_widget)
        menu_layout.setContentsMargins(0, 0, 0, 0)
        menu_layout.setSpacing(0)
        buttons = ["New", "Open", "Save", "Help"]
        for btn_text in buttons:
            btn = QPushButton(btn_text)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: red;
                    color: white;
                    border: none;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: darkred;
                }
            """)
            font = QFont()
            font.setBold(True)
            btn.setFont(font)
            btn.clicked.connect(self.btn_click)
            menu_layout.addWidget(btn)
        menu_layout.addStretch()

        # Kontener dla Main i Status
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # Pasek statusu
        self.status_bar = QWidget()
        self.status_bar.setFixedHeight(40)
        self.status_bar.setStyleSheet("background-color: yellow;")
        self.status_label = QLabel("Status")
        self.status_label.setAlignment(Qt.AlignRight)
        status_layout = QHBoxLayout(self.status_bar)
        status_layout.addWidget(self.status_label)
        status_layout.setContentsMargins(5, 10, 5, 10)

        # Główny obszar
        self.main_area = MapPreview()

        # Dodanie Status i Main do content_layout
        self.content_layout.addWidget(self.status_bar)
        self.content_layout.addWidget(self.main_area)

    def _stack_ui(self):
        # Dodanie widgetów do głównego layoutu
        self.main_layout.addWidget(self.menu_widget)
        self.main_layout.addWidget(self.content_widget)
        # Timer do sprawdzania pozycji myszy
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_mouse_position)
        self.timer.start(50)

        # Włączanie śledzenia myszy
        self.setMouseTracking(True)
        self.menu_widget.setMouseTracking(True)

        self.animation = QPropertyAnimation(self.menu_widget, b"maximumWidth")
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)

    def check_mouse_position(self):
        pos = self.mapFromGlobal(QCursor.pos())
        current_max_width = self.menu_widget.maximumWidth()
        current_actual_width = self.menu_widget.width()

        if pos.x() < 0 or pos.y() < 0:
            return

        if pos.x() <= 40 and current_max_width == 40:
            self.animation.setStartValue(self.menu_widget.width())
            self.animation.setEndValue(200)
            self.animation.start()
            self.menu_widget.raise_()  # Ustawia menu nad main

            # self.menu_widget.setMaximumWidth(200)
            # self.menu_widget.setFixedWidth(200)
            # self.menu_widget.update()
            # self.menu_widget.raise_()

        elif (pos.x() > 200 or pos.x() < 0 or
              pos.y() < 0 or pos.y() > self.height()) and current_max_width == 200:
            self.animation.setStartValue(self.menu_widget.width())
            self.animation.setEndValue(40)
            self.animation.start()

            # self.menu_widget.setMaximumWidth(40)
            # self.menu_widget.setFixedWidth(40)
            # self.menu_widget.update()

    def resizeEvent(self, event):
        self.menu_widget.setFixedHeight(self.height())
        super().resizeEvent(event)
    
    def btn_click(self) -> None:
        name = "dev/database.db"
        self.project_opened.emit(name)
    
    @pyqtSlot(str)
    def update_title(self, new_title: str = None) -> None:
        caption = "Verdant Spot"
        if new_title != None:
            caption += ": {}".format(new_title)
        self.setWindowTitle(caption)