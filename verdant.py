import sys
from PyQt5.QtWidgets import QApplication
from view import VerdantMainView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = VerdantMainView()
    view.show()
    sys.exit(app.exec_())