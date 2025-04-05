from PyQt5.QtWidgets import QApplication, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtCore import QByteArray, Qt, QRectF

def as_icon(svg_data: str) -> QIcon:
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

def as_label(svg_data: str, width: int, height: int) -> QLabel:
    svg_renderer = QSvgRenderer(QByteArray(svg_data.encode('utf-8')))
    
    if not svg_renderer.isValid():
        print("Error!")
        return QLabel()

    label = QLabel()
    label.setFixedSize(width, height)  # Ustawienie rozmiaru 200x200 pikseli

    # Renderowanie SVG
    renderer = QSvgRenderer()
    renderer.load(bytearray(svg_data, encoding='utf-8'))  # Wczytanie SVG ze stringa

    # Tworzenie pixmapy o rozmiarze QLabel
    pixmap = QPixmap(height, height)
    pixmap.fill(Qt.transparent)  # Przezroczyste tło

    # Rysowanie SVG na pixmapie z wyśrodkowaniem
    painter = QPainter(pixmap)
    target_rect = QRectF(0, 0, height, height)  # Docelowy obszar renderowania (QRectF)
    renderer.render(painter, target_rect)  # Renderowanie SVG w podanym obszarze
    painter.end()

    # Ustawienie pixmapy w QLabel i wyśrodkowanie
    label.setPixmap(pixmap)
    label.setAlignment(Qt.AlignCenter)  # Wyśrodkowanie zawartości

    return label