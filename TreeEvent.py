import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TreeEvent(QMainWindow):
    def __init__(self):
        super(TreeEvent, self).__init__()
        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['键','值'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0,'根节点')
        root.setText(1,'0')

        child1 = QTreeWidgetItem(root)
        child1.setText(0,'子节点1')
        child1.setText(1, '1')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, '子节点2')
        child2.setText(1, '2')

        child3 = QTreeWidgetItem(child2)
        child3.setText(0, '子节点2-1')
        child3.setText(1, '3')

        self.tree.setColumnWidth(0,150)

        self.tree.clicked.connect(self.onClicked)

        self.setCentralWidget(self.tree)

    def onClicked(self, index):
        print(index.row())
        print('-'*30)
        item = self.tree.currentItem()
        print('key=%s, value=%s' %(item.text(0), item.text(1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TreeEvent()
    main.show()
    sys.exit(app.exec_())