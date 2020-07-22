
'''
1. 关于对话框
2. 错误对话框
3. 警告对话框
4. 提问对话框
5. 消息对话框
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QMessageBox案例')
        self.resize(300, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.button1 = QPushButton('显示关于对话框')
        self.button1.clicked.connect(self.showDialog)
        layout.addWidget(self.button1)

        self.button2 = QPushButton('显示消息对话框')
        self.button2.clicked.connect(self.showDialog)
        layout.addWidget(self.button2)

        self.button3 = QPushButton('显示警告对话框')
        self.button3.clicked.connect(self.showDialog)
        layout.addWidget(self.button3)

        self.button4 = QPushButton('显示错误对话框')
        self.button4.clicked.connect(self.showDialog)
        layout.addWidget(self.button4)

        self.button5 = QPushButton('显示提问对话框')
        self.button5.clicked.connect(self.showDialog)
        layout.addWidget(self.button5)

    def showDialog(self):
        text = self.sender().text()
        if text == '显示关于对话框':
            QMessageBox.about(self, '关于', '这是一个关于对话框')
        elif text == '显示消息对话框':
            QMessageBox.information(self, '', '这是一个消息对话框', QMessageBox.Yes | QMessageBox.No)
        elif text == '显示警告对话框':
            QMessageBox.warning(self, '警告', '这是一个警告对话框', QMessageBox.Yes | QMessageBox.No)
        elif text == '显示错误对话框':
            QMessageBox.critical(self, '错误', '这是一个错误对话框', QMessageBox.Yes | QMessageBox.No)
        elif text == '显示提问对话框':
            QMessageBox.question(self, '提问', '这是一个提问对话框', QMessageBox.Yes | QMessageBox.No)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMessageBoxDemo()
    main.show()
    sys.exit(app.exec_())



