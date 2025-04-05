from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from svg import as_icon
from .icons import ICONS

def create_menu_button(caption: str, icon: str = "DEFAULT") -> QPushButton:
    button = QPushButton(caption)

    button.setStyleSheet("""
        QPushButton {
            color: black;
            border: none;
            padding: 10px;
            text-align: left;
        }
        QPushButton:hover {
            background-color: gray;
        }
    """)    
    font = QFont()
    font.setBold(True)
    button.setFont(font)

    button.setIcon(as_icon(ICONS[icon]))
    return button

def create_toolbar_button(caption: str) -> QPushButton:
    button = QPushButton(caption)
    button.setFixedHeight(35)
    button.setFixedWidth(35)
   
    font = QFont()
    font.setBold(True)
    button.setFont(font)
    return button