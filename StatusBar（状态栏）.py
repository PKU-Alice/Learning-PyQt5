import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class StatusBar(QMainWindow):
    def __init__(self):
        super(StatusBar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('状态栏演示')
        self.resize(300,200)

        # addToolBar(self, str)
        toolBar = self.addToolBar('')
        # QAction(QIcon, str, parent: QObject = None)
        new = QAction(QIcon('ICO/Xmp.ico'), '新建',self)
        toolBar.addAction(new)
        toolBar.actionTriggered.connect(self.processTrigger)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def processTrigger(self, a):
        # showMessage(self, str, msecs: int = 0)
        self.statusBar.showMessage(a.text() + '被点击了', 500)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StatusBar()
    main.show()
    sys.exit(app.exec_())