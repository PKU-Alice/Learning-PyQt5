import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ModifyTree(QWidget):
    def __init__(self):
        super(ModifyTree, self).__init__()

        layout = QHBoxLayout()

        self.tree = QTreeWidget()
        self.tree.setColumnWidth(0, 150)
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['键', '值'])

        addBtn = QPushButton('添加节点')
        updateBtn = QPushButton('修改节点')
        deleteBtn = QPushButton('删除节点')

        layout.addWidget(addBtn)
        layout.addWidget(updateBtn)
        layout.addWidget(deleteBtn)

        addBtn.clicked.connect(self.addNode)
        updateBtn.clicked.connect(self.updateNode)
        deleteBtn.clicked.connect(self.deleteNode)

        root = QTreeWidgetItem(self.tree)
        root.setText(0, '根节点')
        root.setText(1, '0')

        child1 = QTreeWidgetItem(root)
        child1.setText(0, '子节点1')
        child1.setText(1, '1')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, '子节点2')
        child2.setText(1, '2')

        child3 = QTreeWidgetItem(child2)
        child3.setText(0, '子节点2-1')
        child3.setText(1, '3')

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layout)
        mainLayout.addWidget(self.tree)
        self.setLayout(mainLayout)

    # 添加节点
    def addNode(self):
        item = self.tree.currentItem()
        node = QTreeWidgetItem(item)
        node.setText(0,'新节点')

    def updateNode(self):
        item = self.tree.currentItem()
        item.setText(0,'修改节点')

    def deleteNode(self):
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ModifyTree()
    main.show()
    sys.exit(app.exec_())