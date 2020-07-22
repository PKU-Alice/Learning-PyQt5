'''
显示二维数据表(QTableView控件)
数据源
Model
需要创建QTableView实例和一个数据源(Model)，然后将两者关联
MVC:Model Viewer Controller
MVC的目的是将后端的数据和前端页面的耦合度降低
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class TableView(QWidget):
    def __init__(self):
        super(TableView, self).__init__()
        self.resize(500,300)

        self.model = QStandardItemModel(4, 3)    # 4行3列
        # 设置表的字段
        self.model.setHorizontalHeaderLabels(['id','姓名','年龄'])

        self.tableView = QTableView()
        # 关联QTableView控件和Model
        self.tableView.setModel(self.model)
        self.tableView.clicked.connect(self.clicked)

        # 添加数据
        item11 = QStandardItem('10')
        item12 = QStandardItem('雷神')
        item13 = QStandardItem('2000')

        self.model.setItem(0, 0, item11)
        self.model.setItem(0, 1, item12)
        self.model.setItem(0, 2, item13)

        item31 = QStandardItem('30')
        item32 = QStandardItem('神奇女侠')
        item33 = QStandardItem('300')

        self.model.setItem(2, 0, item31)
        self.model.setItem(2, 1, item32)
        self.model.setItem(2, 2, item33)

        layout = QHBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)

    def clicked(self,item):
        print(item.row())
        print(item.column())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableView()
    main.show()
    sys.exit(app.exec_())