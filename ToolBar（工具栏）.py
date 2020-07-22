'''
工具栏默认按钮：只显示图标，将文本作为悬停提示

工具栏按钮有三种显示状态：
1。 只显示图标
2. 只显示文本
3。 同时显示文本和图标
'''

import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ToolBar(QMainWindow):
    def __init__(self):
        super(ToolBar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('工具栏例子')
        self.resize(300,200)

        tb = self.addToolBar('')
        #  QAction(QIcon, str, parent)
        new = QAction(QIcon('ICO/Xmp.ico'), '新建',self)
        tb.addAction(new)
        open = QAction('打开',self)
        tb.addAction(open)

        # tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        tb.actionTriggered.connect(self.toolbtnpressed)

    def toolbtnpressed(self, a):
        print(a)
        print('按下的工具栏按钮是：',a.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ToolBar()
    main.show()
    sys.exit(app.exec_())