from PyQt5 import QtWidgets, QtCore


class myQLineEdit(QtWidgets.QLineEdit):

    def __int__(self, parent):
        super(myQLineEdit, self).__int__(self)
        # QtWidgets.QLineEdit.__init__(self)
        self.parent = parent

    def keyPressEvent(self, QKeyEvent):
        QtWidgets.QLineEdit.keyPressEvent(self, QKeyEvent)
        print('enter press', QKeyEvent)
        if self.toPlainText() != '':
            print('success')
            self.parent.dealMessage()
        if QKeyEvent.key() == QtCore.Qt.Key_Return:
            print('success press enter key', self.parent.toPlainText())


class myTextEdit(QtWidgets.QTextEdit):  # 继承 原本组件
    def __init__(self, parent):
        QtWidgets.QTextEdit.__init__(self)
        self.parent = parent

    def keyPressEvent(self, event):
        QtWidgets.QTextEdit.keyPressEvent(self, event)
        print('press', event)
        if event.key() == QtCore.Qt.Key_Return:  # 如果是Enter 按钮
            print('success press enter key', self.toPlainText())
