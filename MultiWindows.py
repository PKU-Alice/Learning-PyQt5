import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MultiWindows(QMainWindow):
    def __init__(self):
        super(MultiWindows, self).__init__()

        self.mdi = QMdiArea()
        bar = self.addToolBar('')
        file = bar.addAction('File')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MultiWindows()
    main.show()
    sys.exit(app.exec_())