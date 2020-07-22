import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()
        self.resize(600,600)
        self.setWindowTitle('堆栈窗口控件')

        self.list = QListWidget()
        self.list.addItem('联系方式')
        # insertItem(self, int, str)
        self.list.insertItem(1,'个人信息')
        self.list.insertItem(2,'教育程度')

        self.stack = QStackedWidget()
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()

        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        hbox = QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addWidget(self.stack)
        self.setLayout(hbox)

        self.list.currentRowChanged.connect(self.display)

    def display(self,index):
        # print(self.list.currentItem().text())
        self.stack.setCurrentIndex(index)

    def stack1UI(self):
        layout = QFormLayout()
        layout.addRow('姓名', QLineEdit())
        layout.addRow('地址', QLineEdit())
        self.stack1.setLayout(layout)

    def stack2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget((QRadioButton('女')))
        layout.addRow(QLabel('性别'), sex)
        layout.addRow('生日', QLineEdit())
        self.stack2.setLayout(layout)

    def stack3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))
        self.stack3.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StackedExample()
    main.show()
    sys.exit(app.exec_())