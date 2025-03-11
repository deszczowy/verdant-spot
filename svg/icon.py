from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtCore import QByteArray, Qt

def as_icon(svg_data: str):
    svg_renderer = QSvgRenderer(QByteArray(svg_data.encode('utf-8')))
    
    if not svg_renderer.isValid():
        print("Error!")
        return QIcon()

    pixmap = QPixmap(64, 64)
    pixmap.fill(Qt.GlobalColor.transparent)

    painter = QPainter(pixmap)
    svg_renderer.render(painter)
    painter.end()

    return QIcon(pixmap)