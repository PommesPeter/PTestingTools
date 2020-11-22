
from Pwidgets.gui_utils.main_gui import MainUI
from Pwidgets.gui_utils.show_result import *
import sys

load_table()

if __name__ == '__main__':

    Gui = MainUI()
    Gui.show()
    sys.exit(Gui.exec_())