import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(200,200)
        layout = QVBoxLayout()
        self.colorButton = QPushButton('设置颜色')
        self.colorButton.clicked.connect(self.getColor)
        layout.addWidget(self.colorButton)

        self.colorLabel = QLabel('Hello,测试颜色例子')
        layout.addWidget(self.colorLabel)

        self.colorButton1 = QPushButton('设置背景色')
        self.colorButton1.clicked.connect(self.getBGColor)
        layout.addWidget(self.colorButton1)

        self.setLayout(layout)

    def getBGColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window, color)  # Window设置label的背景色
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(p)

    def getColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        # 给QPalette对象设置颜色, setColor(self, QPalette.ColorRole, Union[QColor, Qt.GlobalColor, QGradient])
        p.setColor(QPalette.WindowText, color)  # WindowText设置label的前景色
        self.colorLabel.setPalette(p)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())