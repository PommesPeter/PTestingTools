
from PyQt5 import QtWidgets
from gui_utils.main_gui import MainUI
from gui_utils.show_result import *
from utils.utils import *
import sys



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUI()
    gui.show()
    tools = Tools()

    factor_num = gui.factor_box.toPlainText()
    print(factor_num)
    line_normal = tools.load_normal_table()
    for line in line_normal:
        li = list(line.split(' '))
        print(li)
    sys.exit(app.exec_())
"""
服务器:IIS,Apache,Jetty  
操作系统:win10,Linux,win7
插件:无,小程序,微信插件
浏览器:IE11,Chrome,Firefox

IIS,Apache,Jetty  
win10,Linux,windows7
无,小程序,微信插件
IE11,Chrome,Firefox
"""

