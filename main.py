
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
服务器:IIS,Apache,Jetty,ubuntu
操作系统:win10,Linux,win7,vista
插件:微信插件
浏览器:IE11
CPU:i7
GPU:rtx2080

2^4 4^1
4个2
1个4
IIS,Apache
win10,Linux
小程序,微信插件
Chrome,Firefox
i3,i5,i7,AMD

3^4
4个3
IIS,Apache,Jetty
win10,Linux,win7
无,小程序,微信插件
IE11,Chrome,Firefox

IIS Apache Jetty  
win10 Linux win7
无 小程序 微信插件
IE11 Chrome Firefox

2^32 32^1
小明,小红
男,女
高,矮
胖,瘦
黑,白
甜食,辣椒
9号,10号
32,16
2003,2010
红烧狮子头,白菜汤
火,冰
小明,小红
男,女
高,矮
胖,瘦
黑,白
甜食,辣椒
9号,10号
32,16
2003,2010
红烧狮子头,白菜汤
火,冰
小明,小红
男,女
高,矮
胖,瘦
黑,白
甜食,辣椒
9号,10号
32,16
2003,2010
黑,白
红,白,黑,橙,紫,赤,黄,绿,青,蓝,紫,淀,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t

"""

