
from gui_utils.main_gui import MainUI
from PyQt5 import QtWidgets, QtCore
import sys


if __name__ == '__main__':

    widget = QtWidgets.QApplication(sys.argv)
    Gui = MainUI()
    Gui.show()
    sys.exit(widget.exec_())