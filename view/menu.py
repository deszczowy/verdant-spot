from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QCursor, QPainter, QPixmap
from .tools import *
from .icons import ICONS
from svg import as_label

class VMainMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__timer = QTimer(self)

        self.__setup_view_attributes()
        self.__start_timer()
        self.__setup_animation()
        self.__create_logo()
        self.__create_buttons()
        self.__stack_components()
    
    def __start_timer(self) -> None:
        self.__timer.timeout.connect(self.__check_mouse_position)
        self.__timer.start(50)

    def __setup_view_attributes(self) -> None:
        self.original_pixmap = QPixmap("res/menu.png")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setObjectName("MenuPanel")
        self.current_width = 40
        self.setMinimumWidth(self.current_width)
        self.setMaximumWidth(self.current_width)
        self.setMouseTracking(True)
    
    def __setup_animation(self) -> None:
        self.animation = QPropertyAnimation(self, b"maximumWidth")
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)

    def __create_logo(self) -> None:
        svg_data = ICONS["LOGO"]
        self.logo = as_label(svg_data, 200, 100)

    def __create_buttons(self) -> None:
        self.new_btn = create_menu_button("New")
        self.open_btn = create_menu_button("Open")
        self.save_btn = create_menu_button("Save")
        self.settings_btn = create_menu_button("Settings")
    
    def __stack_components(self) -> None:
        l = QVBoxLayout(self)
        l.setContentsMargins(0, 0, 0, 0)
        l.setSpacing(0)
        
        l.addStretch()
        
        l.addWidget(self.logo)
        l.addWidget(self.new_btn)
        l.addWidget(self.open_btn)
        l.addWidget(self.save_btn)
        l.addWidget(self.settings_btn)

        l.addStretch()

    def reposition(self):
        if self.parent():
            parent_height = self.parent().height()
            self.setGeometry(0, 0, self.current_width, parent_height)
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self.current_width)
            self.animation.start()
            self.raise_()

    def paintEvent(self, event):
        painter = QPainter(self)
        w = self.width()
        h = self.height()

        aspect_ratio = self.original_pixmap.width() / self.original_pixmap.height()
        scaled_width = int(h * aspect_ratio)

        scaled_pixmap = self.original_pixmap.scaled(
            scaled_width, h
        )

        x = 0
        while x < w:
            painter.drawPixmap(x, 0, scaled_pixmap)
            x += scaled_width

    def __check_mouse_position(self):
        pos = self.mapFromGlobal(QCursor.pos())
        current_max_width = self.maximumWidth()

        if pos.x() < 0 or pos.y() < 0:
            return

        if pos.x() <= 40 and self.current_width == 40:
            self.current_width = 200
        elif (pos.x() > 200 or pos.x() < 0 or
              pos.y() < 0 or pos.y() > self.height()) and self.current_width == 200:
            self.current_width = 40
        self.reposition()