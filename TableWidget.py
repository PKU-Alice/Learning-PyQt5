'''
扩展的表格控件
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(500, 300)
        layout = QHBoxLayout()

        self.tableWidget = QTableWidget()

        # 设置行列数
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)

        layout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['姓名','年龄','籍贯'])

        nameItem = QTableWidgetItem('小明')
        self.tableWidget.setItem(0,0,nameItem)

        # 合并单元格
        self.tableWidget.setSpan(0,0,2,1)

        ageItem = QTableWidgetItem('24')
        ageItem.setTextAlignment(Qt.AlignRight)
        self.tableWidget.setItem(0,1,ageItem)
        jgItem = QTableWidgetItem('北京')
        self.tableWidget.setItem(0,2,jgItem)

        nameItem3 = QTableWidgetItem('白菜')
        self.tableWidget.setItem(2,0,nameItem3)
        ageItem3 = QTableWidgetItem('19')
        self.tableWidget.setItem(2,1,ageItem3)
        jgItem3 = QTableWidgetItem('安庆')

        jgItem3.setFont(QFont('YouYuan', 40, QFont.ExtraBold))
        self.tableWidget.setItem(2,2,jgItem3)

        newItem = QTableWidgetItem(QIcon('./ICO/disc.png'),'光盘')

        self.tableWidget.setItem(3, 1, newItem)

        self.button = QPushButton('排序')
        self.button.clicked.connect(self.order)
        layout.addWidget(self.button)

        self.orderType = Qt.DescendingOrder

        # 禁止编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 整行选择
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 调整行宽自适应文字
        # self.tableWidget.resizeColumnsToContents()

        # setIconSize((height, width))
        self.tableWidget.setIconSize(QSize(40, 40))

        # 调整行高
        self.tableWidget.setRowHeight(3, 50)

        self.setLayout(layout)

    def order(self):
        if self.orderType == Qt.DescendingOrder:
            self.orderType = Qt.AscendingOrder
        else:
            self.orderType = Qt.DescendingOrder
        self.tableWidget.sortItems(1, self.orderType)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableWidgetDemo()
    main.show()
    sys.exit(app.exec_())
