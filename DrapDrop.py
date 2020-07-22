'''
让控件支持拖拽动作
'''

import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyComboBox(QComboBox):
    def __init__(self):
        super(MyComboBox, self).__init__()
        self.setAcceptDrops(True)   # 让它能够接收控件

    def dragEnterEvent(self, QDragEnterEvent):
        print(QDragEnterEvent.mimeData().text())
        if QDragEnterEvent.mimeData().hasText():
            QDragEnterEvent.accept()
        else:
            QDragEnterEvent.ignore()

    def dropEvent(self, QDropEvent):
        self.addItem(QDropEvent.mimeData().text())

class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo, self).__init__()
        formLayout = QFormLayout()
        label = QLabel('请将左边的文本拖拽到右边的下拉列表')
        label.setFont(QFont('YouYuan',15,QFont.Bold))
        formLayout.addRow(label)
        lineEdit = QLineEdit()
        lineEdit.setPlaceholderText('123456')

        lineEdit.setDragEnabled(True)       # 设置可以拖动

        combo = MyComboBox()
        formLayout.addRow(lineEdit, combo)
        self.setLayout(formLayout)

        self.setWindowTitle('拖拽案例')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrapDropDemo()
    main.show()
    sys.exit(app.exec_())