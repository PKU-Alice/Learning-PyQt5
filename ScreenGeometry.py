import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QIcon
def onClick():
    print(widget.x())       # 600 窗口横坐标
    print(widget.y())       # 300 窗口纵坐标
    print(widget.width())  # 280 工作区宽度
    print(widget.height())  # 240 工作区高度
    print('--------------------')

    print(widget.geometry().x())  # 600 工作区横坐标
    print(widget.geometry().y())  # 322 工作区纵坐标
    print(widget.geometry().width())  # 280 工作区宽度
    print(widget.geometry().height())  # 240 工作区高度
    print('--------------------')

    print(widget.frameGeometry().x())  # 600 窗口横坐标
    print(widget.frameGeometry().y())  # 300 窗口纵坐标
    print(widget.frameGeometry().width())  # 280 窗口宽度
    print(widget.frameGeometry().height())  # 262 窗口高度

app = QApplication(sys.argv)

widget = QWidget()
btn = QPushButton(widget)
btn.setText('按钮')
btn.setGeometry(100,0,100,30)
btn.clicked.connect(onClick)

widget.resize(280, 240)      # 设置工作区的尺寸

widget.move(600, 300)
widget.setWindowIcon(QIcon('./ico/QQ.ico'))

widget.setWindowTitle('屏幕坐标系')
widget.show()
sys.exit(app.exec_())

