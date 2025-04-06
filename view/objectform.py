import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout,
                            QComboBox, QLineEdit, QTextEdit, QPushButton,
                            QMessageBox, QHBoxLayout)

class VObjectForm(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.layer_combo = QComboBox()
        #self.layer_combo.addItems(self.layers.values())
        layout.addWidget(self.layer_combo)

        self.type_combo = QComboBox()
        #self.type_combo.addItems(self.object_types.values())
        layout.addWidget(self.type_combo)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nazwa obiektu")
        layout.addWidget(self.name_input)

        self.coords_input = QTextEdit()
        self.coords_input.setPlaceholderText("Wpisz współrzędne (x,y w osobnych liniach)")
        layout.addWidget(self.coords_input)

        button_layout = QHBoxLayout()

        self.clear_button = QPushButton("Wyczyść")
        self.clear_button.clicked.connect(self.clear_form)
        button_layout.addWidget(self.clear_button)

        self.next_button = QPushButton("Następny")
        self.next_button.clicked.connect(self.next_object)
        button_layout.addWidget(self.next_button)

        self.add_button = QPushButton("Dodaj")
        self.add_button.clicked.connect(self.add_data)
        button_layout.addWidget(self.add_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def clear_form(self):
        self.layer_combo.setCurrentIndex(0)
        self.type_combo.setCurrentIndex(0)
        self.name_input.clear()
        self.coords_input.clear()

    def validate_coordinates(self, coords_text):
        lines = coords_text.strip().split('\n')
        invalid_lines = []

        for i, line in enumerate(lines, 1):
            if not line.strip():
                continue
            parts = line.split(',')
            if len(parts) != 2:
                invalid_lines.append(i)
                continue
            try:
                float(parts[0].strip())
                float(parts[1].strip())
            except ValueError:
                invalid_lines.append(i)

        return invalid_lines

    def parse_coordinates(self, coords_text):
        coordinates = []
        lines = coords_text.strip().split('\n')

        for i, line in enumerate(lines, 1):
            if not line.strip():
                continue
            x, y = map(float, line.split(','))
            coordinates.append((x, y, i))
        return coordinates

    def next_object(self):
        self.add()
        self.clear_form()

    def add_data(self):
        self.add()
        self.close()
    
    def add(self):
        # Pobranie danych z formularza
        layer_id = list(self.layers.keys())[self.layer_combo.currentIndex()]
        type_id = list(self.object_types.keys())[self.type_combo.currentIndex()]
        name = self.name_input.text().strip()
        coords_text = self.coords_input.toPlainText()

        # Walidacja współrzędnych
        invalid_lines = self.validate_coordinates(coords_text)
        if invalid_lines:
            QMessageBox.warning(self, "Błąd",
                              f"Błędne współrzędne w liniach: {', '.join(map(str, invalid_lines))}")
            return

        # Tworzenie obiektu danych
        coordinates = self.parse_coordinates(coords_text)

        # Pokazanie informacji o utworzonym obiekcie
        QMessageBox.information(self, "Sukces",
                              f"Utworzono obiekt:\n{str(self.last_object)}")