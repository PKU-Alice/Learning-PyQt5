# QDesktopWidget
import sys
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget, QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon

class QuitApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QuitApp')
        self.resize(400, 300)

        # 添加Button
        self.button = QPushButton('退出')
        self.button.clicked.connect(self.onClickButton)

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        mainframe = QWidget()
        mainframe.setLayout(layout)

        # setCentralWidget(self, mainWidget)
        self.setCentralWidget(mainframe)

    # 按钮单击事件的方法（自定义的slot）
    def onClickButton(self):
        # sender = self.sender()
        # print(sender.text()+'被按下')
        # app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApp()
    main.show()
    sys.exit(app.exec_())
