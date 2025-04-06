from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QTreeView, QPushButton
from .objectform import VObjectForm

class VDataDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data")
        self.__build_ui()

    def __build_ui(self) -> None:
        main_layout = QVBoxLayout(self)
        main_layout.addLayout(self.__data_views())
        main_layout.addLayout(self.__button_bar())
    
    def __data_views(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        self.tree = QTreeView()
        self.form = VObjectForm()
        layout.addWidget(self.tree)
        layout.addWidget(self.form)
        return layout

    def __button_bar(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.addStretch()
        button = QPushButton("Quit")
        button.clicked.connect(self.__quit_button_click)
        layout.addWidget(button)
        return layout
    
    def __quit_button_click(self) -> None:
        self.hide()