'''
校验器：限制文本输入框可以输入的文本类型
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp

class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校验器')

        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        formLayout.addRow('整数类型', intLineEdit)
        formLayout.addRow('浮点类型', doubleLineEdit)
        formLayout.addRow('数字和字母', validatorLineEdit)


        # 整数校验器
        intValidator = QIntValidator()
        intValidator.setRange(1, 99)

        # 浮点校验器，精度：小数点后2位
        doubleValidator = QDoubleValidator()
        doubleValidator.setRange(-360, 360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)

        # 数字和字母校验器
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator()
        validator.setRegExp(reg)

        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())