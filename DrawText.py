'''
绘图API：绘制文本
1. 文本
2. 各种图形（直线、点、椭圆、弧、扇形、多边形等）
3. 图像
QPainter
调用画板：painter.begin()
painter.end() 绘制结束
必须在paintEvent事件方法中绘制各种元素
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtCore import Qt

class DrawText(QWidget):
    def __init__(self):
        super(DrawText, self).__init__()
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(300,200)

        self.text = 'Python从菜鸟到高手'


    def paintEvent(self, event):
        painter = QPainter()     # QPainter(QPaintDevice)
        painter.begin(self)     # begin(self, QPaintDevice)

        pen = QPen(Qt.red, 3, Qt.DotLine)
        # pen.setStyle(Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20,80,250,80)

        painter.setPen(QColor(255,255,255))
        painter.setFont(QFont('SimSun', 25))
        painter.drawText(event.rect(),Qt.AlignCenter, self.text)

        painter.end()    # end(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawText()
    main.show()
    sys.exit(app.exec_())






