
from PyQt5.QtWidgets import *
import sys

class ListWidgetDemo(QMainWindow):
    def __init__(self):
        super(ListWidgetDemo, self).__init__()
        self.setWindowTitle('QListWidget例子')

        self.listwidget = QListWidget()

        # addItem(self, str)
        self.listwidget.addItem('item1')
        self.listwidget.addItem('item2')
        self.listwidget.addItem('item3')
        self.listwidget.addItem('item4')
        self.listwidget.addItem('item5')

        self.listwidget.itemClicked.connect(self.clicked)

        self.setCentralWidget(self.listwidget)

    def clicked(self,index):
        a = self.listwidget.row(index)
        print('选择了第%d项' %(a+1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ListWidgetDemo()
    main.show()
    sys.exit(app.exec_())