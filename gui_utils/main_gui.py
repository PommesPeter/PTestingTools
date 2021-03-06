# coding: utf-8

import os
import re
import time
import threading
import qtawesome
from PyQt5 import QtCore, QtWidgets, QtGui
from gui_utils.ui_thread import UI_Thread

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.factor_level = ""
        self.final_result = ""
        self.query_result = ""
        self.setWindowIcon(QtGui.QIcon('E:\\Workspace\\Python\\PTestingTools\\gui_utils\\pic\\Tools.png'))

        self.setWindowTitle("PTestingTools")
        self.setFixedSize(1270, 800)
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        self.left_widget = QtWidgets.QWidget(self)
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widget.setStyleSheet('''
            QPushButton{
            border:none;
            color:white;
            }
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:20px;
                font-weight:700;
                font-family: Microsoft YaHei UI;
            }
            QPushButton#left_button:hover{
            border-left:4px solid red;
            font-weight:700;
            }
            QWidget#left_widget{
                background:gray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
                }
        ''')
        self.left_widget.setLayout(self.left_layout)

        self.right_widget = QtWidgets.QWidget(self)
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.right_widget.setLayout(self.right_layout)

        self.main_layout.addWidget(self.left_widget, 1, 0, 12, 2)
        self.main_layout.addWidget(self.right_widget, 1, 2, 12, 10)
        self.setCentralWidget(self.main_widget)

        self.setWindowOpacity(1)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.main_layout.setSpacing(0)
        self.mythread = UI_Thread()
        self.init_button()
        self.init_main_page()
        self.init_generating_table_page()
        self.init_table_query_page()


    def init_button(self):
        self.left_close = QtWidgets.QPushButton("")
        self.left_close.clicked.connect(self.on_close_program)
        self.left_visit = QtWidgets.QPushButton("")
        self.left_mini = QtWidgets.QPushButton("")
        self.left_close.setFixedSize(20, 20)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(20, 20)  # 设置按钮大小
        self.left_mini.setFixedSize(20, 20)  # 设置最小化按钮大小
        self.left_close.setStyleSheet('''
            QPushButton{ 
                background:rgb(250,0,0);
            border-radius:10px;
            }
            QPushButton:hover{
                background:rgb(128,0,0);
            }
            QPushButton:pressed{
                background:rgb(255,0,0);
            }
            ''')
        self.left_visit.setStyleSheet('''
            QPushButton{
                background:rgb(225,225,0);
                border-radius:10px;
            }
            QPushButton:hover{
                background:rgb(128,128,0);
            }
            QPushButton:pressed{
                background:rgb(255,255,0);
            }
        ''')
        self.left_mini.setStyleSheet('''
            QPushButton{
                background:rgb(0,225,0);
                border-radius:10px;
            }
            QPushButton:hover{
                background:green;
            }
            QPushButton:pressed{
                background:rgb(0,255,0);
            }
        ''')

        self.left_label_main_page_label = QtWidgets.QPushButton("首页")
        self.left_label_main_page_label.setObjectName("left_label")
        self.left_label_function_page = QtWidgets.QPushButton("功能")
        self.left_label_function_page.setObjectName("left_label")

        self.left_button_main_page = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='white'), "首页")
        self.left_button_main_page.setObjectName('left_button')
        self.left_button_main_page.clicked.connect(self.on_button_main_page_switch)
        self.left_button_generating_table = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "用例生成")
        self.left_button_generating_table.setObjectName('left_button')
        self.left_button_generating_table.clicked.connect(self.on_button_generating_table_page_switch)
        self.left_button_searching_table = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "正交表查询")
        self.left_button_searching_table.setObjectName('left_button')
        self.left_button_searching_table.clicked.connect(self.on_button_query_page_switch)
        self.left_button_history_table = QtWidgets.QPushButton(qtawesome.icon('fa.history', color='white'), "历史记录")
        self.left_button_history_table.setObjectName('left_button')

        self.left_layout.addWidget(self.left_mini, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_label_main_page_label, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_main_page, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_function_page, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_generating_table, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_searching_table, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_history_table, 6, 0, 1, 3)

    def init_input_box(self):
        self.right_bar_widget = QtWidgets.QWidget()
        self.right_bar_layout = QtWidgets.QGridLayout()
        self.right_bar_widget.setLayout(self.right_bar_layout)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

    def init_main_page(self):
        # self.main_page_frame = QtWidgets.QFrame()
        self.right_subwidgets = QtWidgets.QFrame()
        # self.software_title = QtWidgets.QWidget()
        self.right_subwidgets_layout = QtWidgets.QGridLayout()
        # 添加组件，往right_software_title
        self.right_subwidgets.setLayout(self.right_subwidgets_layout)

        self.img = QtGui.QPixmap('E:/Workspace/Python/PTestingTools/gui_utils/pic/2.png')
        self.img_label = QtWidgets.QLabel()
        self.img_label.setObjectName("img_label")
        self.img_label.setPixmap(self.img)
        self.img_label.setStyleSheet('''
            QLabel{
                margin-bottom: 225px;
            }
        ''')

        self.about_button = QtWidgets.QPushButton("关于我")
        self.about_button.setObjectName("about_button")
        self.about_button.setStyleSheet('''
            QPushButton#about_button {
                width: 20px;
                height: 40px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size: 25px;
            }
            QPushButton#about_button:hover{
                width: 20px;
                height: 40px;
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton#about_button:pressed{
                width: 20px;
                height: 40px;
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.about_button.clicked.connect(self.on_about_msg_box)

        self.network_testing_button = QtWidgets.QPushButton("网络环境测试")
        self.network_testing_button.setObjectName("network_testing_button")
        self.network_testing_button.setStyleSheet('''
            QPushButton#network_testing_button {
                width: 20px;
                height: 40px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size: 25px;
            }
            QPushButton#network_testing_button:hover{
                width: 20px;
                height: 40px;
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton#network_testing_button:pressed{
                width: 20px;
                height: 40px;
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.network_testing_button.clicked.connect(self.on_network_testing)

        self.introduction_background = QtWidgets.QLabel()
        self.introduction_background.setObjectName("introduction_background")

        self.right_subwidgets_layout.addWidget(self.img_label, 1, 0, 1, 5)
        self.right_subwidgets_layout.addWidget(self.about_button, 4, 4, 1, 1)
        self.right_subwidgets_layout.addWidget(self.network_testing_button, 4, 3, 1, 1)
        self.right_layout.addWidget(self.right_subwidgets, 0, 0, 1, 9)

    def init_generating_table_page(self):
        self.right_bar_widget = QtWidgets.QFrame()
        self.right_bar_layout = QtWidgets.QGridLayout()
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '水平数^因素数  ')
        self.search_icon.setFont(qtawesome.font('fa', 25))
        self.search_icon.setStyleSheet('''
            QLabel{
                margin-top:30px;
                font-size: 25px;
            }
        ''')
        self.right_search_widget_input = QtWidgets.QLineEdit()
        self.right_search_widget_input.setPlaceholderText("请输入水平数^因素数")
        self.right_search_widget_input.setStyleSheet('''
            QLineEdit{
                    border:1px solid gray;
                    width:250px;
                    border-radius:10px;
                    margin-top: 30px;
                    font-size: 25px;
                    font-family: Microsoft YaHei UI;
            }
            ''')
        self.factor_box = QtWidgets.QPlainTextEdit(self)
        self.output_box = QtWidgets.QPlainTextEdit(self)
        self.box_layout = QtWidgets.QHBoxLayout()
        self.factor_box.setLayout(self.box_layout)
        self.output_box.setLayout(self.box_layout)
        self.factor_box.setPlaceholderText("请输入每一个因素对应的水平，用逗号隔开")
        self.output_box.setPlaceholderText("生成的样例在此处显示")
        self.output_box.setReadOnly(True)
        self.factor_box.setStyleSheet('''
            QPlainTextEdit{
                border:3px solid gray;
                height: 50px;
                border-radius:5px;
                padding: 5px;
                font-size: 25px;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.output_box.setStyleSheet('''
           QPlainTextEdit{
               border:3px solid gray;
               height: 50px;
               border-radius:5px;
               padding 5px;
               font-size: 25px;
               font-family: Microsoft YaHei UI;
           }
        ''')

        self.factor_box_label = QtWidgets.QLabel("水平因素框")
        self.factor_box_label.setStyleSheet('''
            QLabel {
                font-family: Microsoft YaHei UI;
                font-size: 30px;
            }
        ''')
        self.output_box_label = QtWidgets.QLabel("样例生成框")
        self.output_box_label.setStyleSheet('''
            QLabel {
                font-family: Microsoft YaHei UI;
                font-size: 30px;
            }
        ''')
        self.commit_button = QtWidgets.QPushButton("生成测试用例")
        self.commit_button.setObjectName("generate_button")
        self.commit_button.setStyleSheet('''
            QPushButton#generate_button{
                width: 20px;
                height: 40px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size: 25px;
            }
            QPushButton#generate_button:hover{
                width: 30px;
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton#generate_button:pressed{
                width: 30px;
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.reset_button = QtWidgets.QPushButton("重置")
        self.reset_button.setObjectName("reset_button")
        self.reset_button.setStyleSheet('''
            QPushButton#reset_button{
                width: 20px;
                height: 40px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size: 25px;
            }
            QPushButton#reset_button:hover{
                width: 30px;
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton#reset_button:pressed{
                width: 30px;
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')

        self.import_factor_button = QtWidgets.QPushButton("导入")
        self.import_factor_button.setObjectName("import_button")
        self.import_factor_button.clicked.connect(self.on_import_factor_button)
        self.export_sample_button = QtWidgets.QPushButton("导出")
        self.export_sample_button.setObjectName("export_button")
        self.export_sample_button.clicked.connect(self.on_export_sample_button)

        self.import_factor_button.setStyleSheet('''
            QPushButton#import_button{
                width: 20px;
                height: 40px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size: 25px;
            }
            QPushButton#import_button:hover{
                width: 20px;
                height: 40px;
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton#import_button:pressed{
                width: 20px;
                height: 40px;
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.export_sample_button.setStyleSheet('''
            QPushButton#export_button{
                width: 20px;
                height: 40px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size: 25px;
            }
            QPushButton#export_button:hover{
                width: 20px;
                height: 40px;
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton#export_button:pressed{
                width: 20px;
                height: 40px;
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.commit_button.clicked.connect(self.on_commit_factor_num)
        self.reset_button.clicked.connect(self.on_button_reset_input_box)
        self.right_bar_layout.addWidget(self.search_icon, 1, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_search_widget_input, 1, 1, 1, 5)
        self.right_bar_layout.addWidget(self.factor_box_label, 2, 0, 1, 1)
        self.right_bar_layout.addWidget(self.output_box_label, 2, 3, 1, 1)
        self.right_bar_layout.addWidget(self.import_factor_button, 3, 2, 1, 1)
        self.right_bar_layout.addWidget(self.export_sample_button, 3, 6, 1, 1)
        self.right_bar_layout.addWidget(self.factor_box, 4, 0, 3, 3)
        self.right_bar_layout.addWidget(self.output_box, 4, 3, 3, 4)
        self.right_layout.addWidget(self.commit_button, 6, 1, 1, 3)
        self.right_layout.addWidget(self.reset_button, 6, 5, 1, 3)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)
        self.right_bar_widget.setVisible(False)
        self.commit_button.setVisible(False)
        self.reset_button.setVisible(False)

    def init_table_query_page(self):

        self.right_query_widget = QtWidgets.QFrame()
        self.right_query_layout = QtWidgets.QGridLayout()
        self.right_query_widget.setLayout(self.right_query_layout)

        self.search_icon_query = QtWidgets.QLabel(chr(0xf002) + ' ' + '水平数^因素数  ')
        self.search_icon_query.setFont(qtawesome.font('fa', 25))
        self.search_icon_query.setStyleSheet('''
            QLabel{
                margin-top:30px;
                font-size: 25px;
            }
        ''')
        self.right_query_input = QtWidgets.QLineEdit()
        self.right_query_input.setPlaceholderText("请输入水平数^因素数")
        self.right_query_input.setStyleSheet('''
            QLineEdit{
                    border:1px solid gray;
                    width:250px;
                    border-radius:10px;
                    margin-top: 30px;
                    font-size: 25px;
                    font-family: Microsoft YaHei UI;
            }
            ''')
        self.result_box = QtWidgets.QPlainTextEdit(self)
        self.result_box.setLayout(self.box_layout)
        self.result_box.setPlaceholderText("查询的正交表在此处显示")
        self.result_box.setReadOnly(True)
        self.result_box.setStyleSheet('''
           QPlainTextEdit{
               border:3px solid gray;
               height: 50px;
               border-radius:5px;
               padding 5px;
               font-size: 25px;
               font-family: Microsoft YaHei UI;
           }
        ''')
        self.output_box_label = QtWidgets.QLabel("正交表查询结果")
        self.output_box_label.setStyleSheet('''
            QLabel {
                font-family: Microsoft YaHei UI;
                font-size: 30px;
            }
        ''')
        self.query_button = QtWidgets.QPushButton("查找正交表")
        self.query_button.setObjectName("query_button")
        self.query_button.setStyleSheet('''
            QPushButton#query_button{
                width: 20px;
                height: 40px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size: 25px;
            }
            QPushButton#query_button:hover{
                width: 30px;
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton#query_button:pressed{
                width: 30px;
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.reset_query_button = QtWidgets.QPushButton("重置")
        self.reset_query_button.setObjectName("reset_query_button")
        self.reset_query_button.setStyleSheet('''
            QPushButton#reset_query_button{
                width: 20px;
                height: 40px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size: 25px;
            }
            QPushButton#reset_query_button:hover{
                width: 30px;
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton#reset_query_button:pressed{
                width: 30px;
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.export_query_button = QtWidgets.QPushButton("导出")
        self.export_query_button.setObjectName("export_query_button")
        self.query_button.clicked.connect(self.on_query_table)
        self.reset_query_button.clicked.connect(self.on_button_reset_input_box_query)
        self.export_query_button.clicked.connect(self.on_export_table_button)
        self.export_query_button.setStyleSheet('''
            QPushButton#export_query_button{
                width: 20px;
                height: 40px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size: 25px;
            }
            QPushButton#export_query_button:hover{
                width: 20px;
                height: 40px;
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton#export_query_button:pressed{
                width: 20px;
                height: 40px;
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.right_query_layout.addWidget(self.search_icon_query, 1, 0, 1, 1)
        self.right_query_layout.addWidget(self.right_query_input, 1, 1, 1, 5)
        self.right_query_layout.addWidget(self.output_box_label, 2, 1, 1, 4)
        self.right_query_layout.addWidget(self.export_query_button, 3, 4, 1, 1)
        self.right_query_layout.addWidget(self.result_box, 4, 1, 1, 4)
        self.right_layout.addWidget(self.query_button, 6, 1, 1, 3)
        self.right_layout.addWidget(self.reset_query_button, 6, 5, 1, 3)

        self.right_layout.addWidget(self.right_query_widget, 0, 0, 1, 9)
        self.right_query_widget.setVisible(False)
        self.query_button.setVisible(False)
        self.reset_query_button.setVisible(False)

    def on_button_generating_table_page_switch(self):
        self.right_bar_widget.setVisible(True)
        self.commit_button.setVisible(True)
        self.reset_button.setVisible(True)
        self.query_button.setVisible(False)
        # self.title_widget.setVisible(False)
        self.right_query_widget.setVisible(False)
        self.right_subwidgets.setVisible(False)
        self.reset_query_button.setVisible(False)

    def on_button_main_page_switch(self):
        self.right_bar_widget.setVisible(False)
        self.commit_button.setVisible(False)
        self.reset_button.setVisible(False)
        self.right_query_widget.setVisible(False)
        self.right_subwidgets.setVisible(True)
        self.query_button.setVisible(False)
        self.reset_query_button.setVisible(False)
        # self.title_widget.setVisible(True)

    def on_button_query_page_switch(self):
        self.right_bar_widget.setVisible(False)
        self.commit_button.setVisible(False)
        self.reset_button.setVisible(False)
        self.right_subwidgets.setVisible(False)
        self.right_query_widget.setVisible(True)
        self.query_button.setVisible(True)
        self.reset_query_button.setVisible(True)

    def on_button_reset_input_box(self):
        self.factor_box.setPlainText("")
        self.output_box.setPlainText("")
        self.right_search_widget_input.setText("")

    def on_button_reset_input_box_query(self):
        self.result_box.setPlainText("")
        self.right_query_input.setText("")

    def error_msg_box(self):
        self.error_msgbox = QtWidgets.QMessageBox()
        self.error_msgbox.setWindowTitle("错误")
        self.error_msgbox.setText("输入格式有误，请重新输入！！")
        confirm_button = QtWidgets.QPushButton("确定")
        cancle_button = QtWidgets.QPushButton("取消")
        confirm_button.setStyleSheet('''
            QPushButton{
                width: 60px;
                height: 30px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size:20px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        cancle_button.setStyleSheet('''
            QPushButton{
                width: 60px;
                height: 30px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size:20px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.error_msgbox.addButton(confirm_button, QtWidgets.QMessageBox.YesRole)
        self.error_msgbox.addButton(cancle_button, QtWidgets.QMessageBox.NoRole)
        self.error_msgbox.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.error_msgbox.setStyleSheet('''
            QMessageBox{
                font-family:Microsoft YaHei UI;
                font-size:25px;
                background-color:white;
                border:5px solid gray;
                border-radius:10px;
            }
        ''')
        self.error_msgbox.exec_()
        if self.error_msgbox == QtWidgets.QMessageBox.Yes:
            self.on_button_reset_input_box()
        elif self.error_msgbox == QtWidgets.QMessageBox.No:
            self.on_button_reset_input_box()
        else:
            self.on_button_reset_input_box()

    def empty_msg_box(self):
        self.empty_msgbox = QtWidgets.QMessageBox()
        self.empty_msgbox.setWindowTitle("错误")      
        self.empty_msgbox.setText("水平因素框输入为空，请重新输入！！")
        confirm_button = QtWidgets.QPushButton("确定")
        cancle_button = QtWidgets.QPushButton("取消")
        confirm_button.setStyleSheet('''
            QPushButton{
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size:25px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        cancle_button.setStyleSheet('''
            QPushButton{
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size:25px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.empty_msgbox.addButton(confirm_button, QtWidgets.QMessageBox.YesRole)
        self.empty_msgbox.addButton(cancle_button, QtWidgets.QMessageBox.NoRole)
        self.empty_msgbox.setStyleSheet('''
            QMessageBox{
                font-family:Microsoft YaHei UI;
                font-size:25px;
                background-color:white;
                border:5px solid gray;
                border-radius:10px;
            }
        ''')
        self.empty_msgbox.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.empty_msgbox.exec_()
        if self.empty_msgbox == QtWidgets.QMessageBox.Yes:
            self.on_button_reset_input_box()
        elif self.empty_msgbox == QtWidgets.QMessageBox.Cancel:
            self.on_button_reset_input_box()
        else:
            self.on_button_reset_input_box()

    def not_found_msg_box(self):
        self.not_found_msgbox = QtWidgets.QMessageBox()
        self.not_found_msgbox.setWindowTitle("错误")
        self.not_found_msgbox.setText("输入的水平^因素数错误，未在正交表中找到，请重新输入！！")
        confirm_button = QtWidgets.QPushButton("确定")
        cancle_button = QtWidgets.QPushButton("取消")
        confirm_button.setStyleSheet('''
            QPushButton{
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size:25px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        cancle_button.setStyleSheet('''
            QPushButton{
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size:25px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.not_found_msgbox.addButton(confirm_button, QtWidgets.QMessageBox.YesRole)
        self.not_found_msgbox.addButton(cancle_button, QtWidgets.QMessageBox.NoRole)
        self.not_found_msgbox.setStyleSheet('''
            QMessageBox{
                font-family:Microsoft YaHei UI;
                font-size:25px;
                background-color:white;
                border:5px solid gray;
                border-radius:10px;
            }
        ''')
        self.not_found_msgbox.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.not_found_msgbox.exec_()
        if self.not_found_msgbox == QtWidgets.QMessageBox.Yes:
            self.on_button_reset_input_box()
        elif self.not_found_msgbox == QtWidgets.QMessageBox.Cancel:
            self.on_button_reset_input_box()
        else:
            self.on_button_reset_input_box()

    def error_format_msg_box(self):
        self.error_format_msgbox = QtWidgets.QMessageBox()
        self.error_format_msgbox.setWindowTitle("错误")
        self.error_format_msgbox.setText("输入的因素和水平数与水平^因素框中的不符，请重新输入！！")
        confirm_button = QtWidgets.QPushButton("确定")
        cancle_button = QtWidgets.QPushButton("取消")
        confirm_button.setStyleSheet('''
            QPushButton{
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size:25px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        cancle_button.setStyleSheet('''
            QPushButton{
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size:25px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.error_format_msgbox.addButton(confirm_button, QtWidgets.QMessageBox.YesRole)
        self.error_format_msgbox.addButton(cancle_button, QtWidgets.QMessageBox.NoRole)
        self.error_format_msgbox.setStyleSheet('''
            QMessageBox{
                font-family:Microsoft YaHei UI;
                font-size:25px;
                background-color:white;
                border:5px solid gray;
                border-radius:10px;
            }
        ''')
        self.error_format_msgbox.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.error_format_msgbox.exec_()
        if self.error_format_msgbox == QtWidgets.QMessageBox.Yes:
            self.on_button_reset_input_box()
        elif self.error_format_msgbox == QtWidgets.QMessageBox.Cancel:
            self.on_button_reset_input_box()
            return
        else:
            self.on_button_reset_input_box()

    def export_error_msg_box(self):
        self.error_format_msgbox = QtWidgets.QMessageBox()
        self.error_format_msgbox.setWindowTitle("错误")
        self.error_format_msgbox.setText("当前输出框为空，无法导出！！")
        confirm_button = QtWidgets.QPushButton("确定")
        cancle_button = QtWidgets.QPushButton("取消")
        confirm_button.setStyleSheet('''
            QPushButton{
                width: 60px;
                height: 30px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size:20px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        cancle_button.setStyleSheet('''
            QPushButton{
                width: 60px;
                height: 30px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size:20px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.error_format_msgbox.addButton(confirm_button, QtWidgets.QMessageBox.YesRole)
        self.error_format_msgbox.addButton(cancle_button, QtWidgets.QMessageBox.NoRole)
        self.error_format_msgbox.setStyleSheet('''
            QMessageBox{
                font-family:Microsoft YaHei UI;
                font-size:25px;
                background-color:white;
                border:5px solid gray;
                border-radius:10px;
            }
        ''')
        self.error_format_msgbox.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.error_format_msgbox.exec_()

    def network_status_msg_box(self, content):
        self.network_status_msgbox = QtWidgets.QMessageBox()
        self.network_status_msgbox.setWindowTitle("网络状态")
        self.network_status_msgbox.setText("测试结果\n" + content)
        confirm_button = QtWidgets.QPushButton("确定")
        cancle_button = QtWidgets.QPushButton("取消")
        confirm_button.setStyleSheet('''
            QPushButton{
                width: 60px;
                height: 30px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size:20px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        cancle_button.setStyleSheet('''
            QPushButton{
                width: 60px;
                height: 30px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size:20px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.network_status_msgbox.addButton(confirm_button, QtWidgets.QMessageBox.YesRole)
        self.network_status_msgbox.addButton(cancle_button, QtWidgets.QMessageBox.NoRole)
        self.network_status_msgbox.setStyleSheet('''
            QMessageBox{
                font-family:Consolas;
                font-size:15px;
                background-color:white;
                border:5px solid gray;
                border-radius:10px;
            }
        ''')
        self.network_status_msgbox.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.network_status_msgbox.exec_()

    def find_factor_num_in_table(self, factor_num_str, table):
        result = []
        self.formated_list = []
        factor_num_str_splited = factor_num_str.split('^')
        for str_splited in factor_num_str_splited:
            if len(str_splited) > 1:
                str_splited = str_splited.split(' ')
                for _str in str_splited:
                    self.formated_list.append(_str)
                continue
            self.formated_list.append(str_splited)
        print(self.formated_list)
        if self.formated_list[1] == '':
            self.error_format_msg_box()
            return
        input_level_num = int(self.formated_list[0])
        input_factor_num = int(self.formated_list[1])
        for index, line in enumerate(table):
            if '^' in line:
                table_len = int(line.split(' ')[-1].split('\n')[0].split('n=')[-1])
                self.table_len = table_len
                table_factor_num = line.split(' ')[0]
                self.level_num = int(table_factor_num.split('^')[0])
                self.factor_num = int(table_factor_num.split('^')[1])
                if input_level_num == self.level_num and input_factor_num == self.factor_num:
                    for i in range(index + 1, index + table_len + 1):
                        result.append(table[i].split('\n')[0])
                    break
        if len(result) == 0:
            return None
        return result

    def on_network_testing(self):
        # self.network_testing()
        self.mythread.start()
        address = "baidu.com"
        print("正在尝试连接" + address + "...")
        _str = os.popen('ping ' + address)
        self.network_status_msg_box(_str.read())


    def on_close_program(self):
        app = QtWidgets.QApplication.instance()
        app.quit()

    def on_minmize_window(self):
        self.main_widget.setWindowState(QtCore.Qt.WindowMinimized)

    def on_maxmize_window(self):
        self.main_widget.setWindowState(QtCore.Qt.WindowMaximized)

    def on_commit_factor_num(self):
        self.factor_num = self.right_search_widget_input.text()
        self.factor_level = self.factor_box.toPlainText()
        # normal table
        if '^' in self.factor_num:
            if self.factor_level is '':
                self.empty_msg_box()
                return
            if '\n' in self.factor_level:
                self.factor_level = self.factor_level.strip()
                print(self.factor_level)
            if '，' in self.factor_level:
                self.factor_level = self.factor_level.replace('，', ',')
            table = Tools.get_table()
            result = self.find_factor_num_in_table(self.factor_num, table)
            # print(self.formated_list)
            if result is None:
                self.not_found_msg_box()
                return
            sample_list = []
            factor_list = []
            outputs = []
            self.final_result = ""
            factor_num_sum = sum([int(x) for x in self.formated_list[1::2]])
            for sample in result:
                if len(sample) - 1 == factor_num_sum:
                    # print(sample[:-2])
                    _sample = [int(x) for x in sample[:-2]]
                    _sample += [int(sample[-2:])]
                    sample_list.append(_sample)
                else:
                    sample_list.append([int(x) for x in sample])
            # self.factor_level = self.factor_box.toPlainText()
            self.factor_level = re.split("\n", self.factor_level)
            # self.factor_level.remove('')
            for factor in self.factor_level:
                factor_list.append(factor.split(','))

            if len(factor_list) != factor_num_sum:
                self.error_format_msg_box()
                return
            for sample in sample_list:
                output = []
                for i, index in enumerate(sample):
                    output.append(factor_list[i][index])
                outputs.append(output)
            for _result in outputs:
                for i, __result in enumerate(_result):
                    if i == len(_result) - 1:
                        self.final_result += (__result + "\n")
                        continue
                    self.final_result += (__result + ",")
            print(self.final_result)
            self.output_box.setPlainText(self.final_result)
        else:
            self.error_msg_box()

    def on_query_table(self):
        self.query_result = ""
        self.factor_num = self.right_query_input.text()
        print(self.factor_num)
        if '^' in self.factor_num:
            table = Tools.get_table()
            result = self.find_factor_num_in_table(self.factor_num, table)
            if result is None:
                self.not_found_msg_box()
                return
            for i, _result in enumerate(result):
                self.query_result += (_result + '\n')
            self.result_box.setPlainText(self.query_result)
        else:
            self.error_msg_box()

    def on_about_msg_box(self):
        self.about_button_msgbox = QtWidgets.QMessageBox()
        self.about_button_msgbox.setWindowTitle("错误")
        self.about_button_msgbox.setText(
            "\n   本工具由1900301236谢浚霖开发，可以实现根据正交表以及输入的水平数和因素数自动生成测试用例。\n\n\n\n\nPommesPeter\t\nEmail:me@pommespeter.com\t\nGithub ID: PommesPeter\t\nTencentQQ: 434596665")
        confirm_button = QtWidgets.QPushButton("确定")
        confirm_button.setStyleSheet('''
            QPushButton{
                width: 60px;
                height: 30px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: Microsoft YaHei UI;
                font-size:20px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Microsoft YaHei UI;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Microsoft YaHei UI;
            }
        ''')
        self.about_button_msgbox.addButton(confirm_button, QtWidgets.QMessageBox.YesRole)
        self.about_button_msgbox.setStyleSheet('''
            QMessageBox {
                font-family:Microsoft YaHei UI;
                font-size:18px;
                background-color:white;
                border:5px solid gray;
                border-radius:10px;
            }
        ''')
        self.about_button_msgbox.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.about_button_msgbox.exec_()

    def on_import_factor_button(self):
        self.factor_level = ""
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, '请选择水平和因素文件', '', 'csv Files (*.csv)')
        if file_name == '':
            return
        with open(file_name, 'r') as f:
            lines = f.readlines()
        print(lines)
        self.right_search_widget_input.setText(lines[0].split('\n')[0])
        for line in lines[1:]:
            self.factor_level += line
        self.factor_box.setPlainText(self.factor_level)

    def on_export_sample_button(self):
        if self.final_result == '':
            self.export_error_msg_box()
            return
        save_path = QtWidgets.QFileDialog.getExistingDirectory(self, "选择保存路径", "./")
        if save_path == '':
            return
        file_list = os.listdir(save_path)
        with open(os.path.join(save_path, 'output_' + str(len(file_list)) + '.csv'), 'a') as f:
            print(self.final_result, file=f)

    def on_export_table_button(self):
        if self.query_result == '':
            self.export_error_msg_box()
            return
        save_path = QtWidgets.QFileDialog.getExistingDirectory(self, "选择保存路径", './')
        if save_path == '':
            return
        file_list = os.listdir(save_path)
        with open(os.path.join(save_path, 'output_table_' + str(len(file_list)) + '.csv'), 'a') as f:
            print(self.query_result, file=f)


class Tools:
    def __init__(self):
        self.table = []
        self.lines = []

    @staticmethod
    def get_table():
        with open("./data/ts723_Designs.txt", "r") as f:
            lines = f.readlines()
        return lines

    @staticmethod
    def get_normal_table():
        with open("./data/ts723_Designs.txt", "r") as f:
            lines = f.readlines()
        return lines[:157]
