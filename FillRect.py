import sys, math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class FillRect(QWidget):
    def __init__(self):
        super(FillRect, self).__init__()
        self.resize(300,600)
        self.setWindowTitle('用画刷填充区域')

    def paintEvent(self, QPaintEvent):
        painter = QPainter()
        painter.begin(self)

        brush = QBrush(Qt.Dense1Pattern)
        painter.setBrush(brush)

        painter.drawRect(100,15,120,120)
        # QBrush(Union[QColor, Qt.GlobalColor, QGradient], style: Qt.BrushStyle = Qt.SolidPattern)
        brush = QBrush(QColor(255,255,120),Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(100, 135, 120, 120)

        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FillRect()
    main.show()
    sys.exit(app.exec_())