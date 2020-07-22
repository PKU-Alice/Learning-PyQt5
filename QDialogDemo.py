'''
对话框：QDialog

QMessageBox
QColorDialog
QFileDialog
QFontDialog
QInputDialog

QMainWindow
QWidget
QDialog

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QDialog案例')
        self.resize(300,200)

        self.button = QPushButton('弹出对话框', self)
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        button = QPushButton('确定', dialog)
        button.clicked.connect(dialog.close)
        button.move(50, 50)
        dialog.setWindowTitle('对话框')
        dialog.setWindowModality(Qt.ApplicationModal)
        '''
        所有对话框窗体的标题栏上没有最小化和最大化控件，且默认为模态窗口。
        如果需要修改该属性，可调用setWindowModality()方法，取值如下：
        Qt.NonModal。非模态，在未关闭对话框时，可以和程序的其他窗口进行交互；
        Qt.WindowModal。模态窗口。用户必须处理完当前对话框，才可以和父窗口交互；
        Qt.ApplicationModal。应用程序级模态，即用户在未处理完当前对话框时，不能和任何其他窗口进行交互。
        '''
        dialog.exec_()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())


