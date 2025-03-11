import sys
from PyQt5.QtWidgets import QApplication
from supervisor import Supervisor

if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = Supervisor()
    s.run()
    sys.exit(app.exec_())