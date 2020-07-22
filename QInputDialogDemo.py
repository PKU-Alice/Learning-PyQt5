'''
输入对话框：QInputDialog
QInputDialog.getItem
QInputDialog.getText
QInputDialog.getInt
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QInputDialogDemo(QWidget):
    def __init__(self):
        super(QInputDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('输入对话框')
        layout = QFormLayout()

        self.button1 = QPushButton('获取列表中的选项')
        self.button1.clicked.connect(self.getItem)
        self.lineEdit1 = QLineEdit()
        layout.addRow(self.button1)
        layout.addRow(self.lineEdit1)

        self.button2 = QPushButton('获取字符串')
        self.button2.clicked.connect(self.getTest)
        self.lineEdit2 = QLineEdit()
        layout.addRow(self.button2)
        layout.addRow(self.lineEdit2)

        self.button3 = QPushButton('获取整数')
        self.button3.clicked.connect(self.getInt)
        self.lineEdit3 = QLineEdit()
        layout.addRow(self.button3)
        layout.addRow(self.lineEdit3)

        self.setLayout(layout)

    def getItem(self):
        items = ('C','C++','Ruby','Python','Java')
        item, ok = QInputDialog.getItem(self, '请选择编程语言', '语言列表', items)
        if item and ok:
            self.lineEdit1.setText(item)


    def getTest(self):
        text, ok = QInputDialog.getText(self, '文本输入框', '输入姓名')
        if text and ok:
            self.lineEdit2.setText(text)

    def getInt(self):
        num, ok = QInputDialog.getInt(self,'整数输入框','数字')
        if ok and num:
            self.lineEdit3.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()
    sys.exit(app.exec_())