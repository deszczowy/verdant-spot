from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QFont, QCursor, QPainter, QPixmap
from svg import as_icon
from .icons import ICONS

class VMainMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.original_pixmap = QPixmap("res/menu.png")
        self.setObjectName("MenuPanel")
        self.current_width = 40
        self.setMinimumWidth(self.current_width)
        self.setMaximumWidth(self.current_width)  # Początkowa szerokość

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_mouse_position)
        self.timer.start(50)

        self.setMouseTracking(True)

        self.animation = QPropertyAnimation(self, b"maximumWidth")
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
    

        # Przyciski w menu
        menu_layout = QVBoxLayout(self)
        menu_layout.setContentsMargins(0, 0, 0, 0)
        menu_layout.setSpacing(0)
        buttons = ["New", "Open", "Save", "Help"]
        for btn_text in buttons:
            btn = QPushButton(btn_text)
            btn.setStyleSheet("""
                QPushButton {
                    color: red;
                    border: none;
                    padding: 10px;
                    text-align: left;
                }
                QPushButton:hover {
                    background-color: darkred;
                }
            """)
            icon = as_icon(ICONS["DEFAULT"])
            font = QFont()
            font.setBold(True)
            btn.setFont(font)
            btn.setIcon(icon)
            ##btn.clicked.connect(self.btn_click)
            menu_layout.addWidget(btn)
        menu_layout.addStretch()

    def reposition(self):
        """Dopasowanie nakładki do lewej strony okna"""
        if self.parent():
            print("repos")
            parent_height = self.parent().height()
            self.setGeometry(0, 0, self.current_width, parent_height)
            #self.setMaximumWidth(self.current_width)
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self.current_width)
            self.animation.start()
            #self.setFixedWidth(self.current_width)
            #self.update()
            self.raise_()
            

    def paintEvent(self, event):
        painter = QPainter(self)
        w = self.width()
        h = self.height()

        # Skalowanie z zachowaniem proporcji do wysokości widgetu
        aspect_ratio = self.original_pixmap.width() / self.original_pixmap.height()
        scaled_width = int(h * aspect_ratio)

        scaled_pixmap = self.original_pixmap.scaled(
            scaled_width, h
        )

        x = 0
        while x < w:
            painter.drawPixmap(x, 0, scaled_pixmap)
            x += scaled_width

    def check_mouse_position(self):
        pos = self.mapFromGlobal(QCursor.pos())
        current_max_width = self.maximumWidth()

        print("cmw {}, caw {}, pos {}".format(current_max_width, self.current_width, pos))
        if pos.x() < 0 or pos.y() < 0:
            return

        if pos.x() <= 40 and self.current_width == 40:
            self.current_width = 200
            #self.animation.setStartValue(self.width())
            #self.animation.setEndValue(200)
            #self.animation.start()
            #self.raise_()  # Ustawia menu nad main
        elif (pos.x() > 200 or pos.x() < 0 or
              pos.y() < 0 or pos.y() > self.height()) and self.current_width == 200:
            self.current_width = 40
            #self.animation.setStartValue(self.width())
            #self.animation.setEndValue(40)
            #self.animation.start()
        self.reposition()
        #self.setMaximumWidth(self.current_width)
        #self.setFixedWidth(self.current_width)
        #self.update()
        #self.raise_()
