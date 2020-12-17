
from PyQt5 import QtWidgets
from gui_utils.main_gui import MainUI, Tools
from gui_utils.show_result import *
from utils.utils import *
import sys



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUI()
    gui.show()
    tools = Tools()
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

