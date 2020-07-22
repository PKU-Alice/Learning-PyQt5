'''
使用剪贴板
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ClipBoard(QDialog):
    def __init__(self):
        super(ClipBoard, self).__init__()

        textCopyButton = QPushButton('复制文本')
        textPasteButton = QPushButton('粘贴文本')

        htmlCopyButton = QPushButton('复制HTML')
        htmlPasteButton = QPushButton('粘贴HTML')

        imageCopyButton = QPushButton('复制图像')
        imagePasteButton = QPushButton('粘贴图像')

        self.textLabel = QLabel('默认文本')
        self.textLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap(''))
        self.imageLabel.setAlignment(Qt.AlignCenter)

        layout = QGridLayout()
        layout.addWidget(textCopyButton,0,0,1,2,Qt.AlignCenter)
        # layout.addWidget(textPasteButton,0,1)
        layout.addWidget(htmlCopyButton,1,0)
        layout.addWidget(htmlPasteButton,1,1)
        layout.addWidget(imageCopyButton,2,0)
        layout.addWidget(imagePasteButton,2,1)

        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)

        layout.addWidget(self.textLabel,3,0,1,2)
        layout.addWidget(self.imageLabel,4,0,1,2)
        self.setLayout(layout)

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('ICO/disc.png'))

    def pasteImage(self):
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ClipBoard()
    main.show()
    sys.exit(app.exec_())