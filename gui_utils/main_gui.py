# coding: utf-8

import re
import qtawesome
from PyQt5 import QtCore, QtWidgets

from gui_utils.custom_widgets import myQLineEdit
from gui_utils.thread_ui import UI_Thread


class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
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
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
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
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')
        self.right_widget.setLayout(self.right_layout)

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)
        self.setCentralWidget(self.main_widget)

        self.setWindowOpacity(1)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.main_layout.setSpacing(0)

        self.init_button()
        self.init_main_page()
        self.init_generating_table_page()
        self.thread_ui = UI_Thread()

    def init_button(self):
        self.left_close = QtWidgets.QPushButton("")
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
        self.left_button_history_table = QtWidgets.QPushButton(qtawesome.icon('fa.history', color='white'), "历史记录")
        self.left_button_history_table.setObjectName('left_button')

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
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
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '水平数^因素数  ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        # self.right_search_widget_input = QtWidgets.QLineEdit()
        self.right_search_widget_input = myQLineEdit(self.right_bar_layout)
        self.right_search_widget_input.setPlaceholderText("请输入水平数^因素数")
        self.right_search_widget_input.setStyleSheet('''
            QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }
            ''')
        # self.right_search_widget_input.returnPressed.connect(self.on_lineEdit_enter)
        # self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        # self.right_bar_layout.addWidget(self.right_search_widget_input, 0, 1, 1, 8)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

    def init_main_page(self):
        # self.main_page_frame = QtWidgets.QFrame()
        self.right_subwidgets = QtWidgets.QFrame()
        # self.software_title = QtWidgets.QWidget()
        self.right_subwidgets_layout = QtWidgets.QGridLayout()
        # 添加组件，往right_software_title
        self.right_subwidgets.setLayout(self.right_subwidgets_layout)

        self.title_widget = QtWidgets.QLabel()
        self.title_widget.setObjectName("title_label")
        self.title_widget.setText("正交表查询工具")
        self.title_widget.setAlignment(QtCore.Qt.AlignHCenter)
        self.title_widget.setStyleSheet('''
            QLabel#title_label {
                border:none;
                color: red;
                font-size:30px;
                font-family: SimSun;
            }
        '''
                                        )

        self.introduction_background = QtWidgets.QLabel()
        self.introduction_background.setObjectName("introduction_background")

        self.introduction_label_widget = QtWidgets.QLabel()
        self.introduction_label_widget.setWordWrap(True)
        self.introduction_label_widget.setObjectName("introduction_label")
        self.introduction_label_widget.setText(
            "本工具由1900301236谢浚霖开发，可以实现根据正交表以及输入的水平数和因素数自动生成测试用例\n")
        self.introduction_label_widget.setStyleSheet('''
            QLabel#introduction_label {
                border-radius:45px;
                font-size: 25px;
                font-family: SimSun;
            }
        ''')

        self.introdcution_label_widget_2 = QtWidgets.QLabel()
        self.introdcution_label_widget_2.setWordWrap(True)
        self.introdcution_label_widget_2.setObjectName("troduction_label_2")
        self.introdcution_label_widget_2.setText(
            "PommesPeter\t\nEmail:me@pommespeter.com\t\nGithub ID: PommesPeter\t\nTencentQQ: 434596665")

        self.introduction_label_widget.resize(50, 50)
        # self.introduction_label_widget_2.resize(50, 50)
        self.right_subwidgets_layout.addWidget(self.title_widget, 2, 1, 2, 5)
        self.right_subwidgets_layout.addWidget(self.introduction_label_widget, 3, 1, 1, 4)
        self.right_subwidgets_layout.addWidget(self.introdcution_label_widget_2, 4, 1, 1, 4)
        self.right_layout.addWidget(self.right_subwidgets, 0, 0, 1, 9)
        self.right_layout.addWidget(self.title_widget, 0, 0, 1, 10)

    def init_generating_table_page(self):
        self.right_bar_widget = QtWidgets.QFrame()
        # self.right_bar_widget = QtWidgets.QWidget()
        self.right_bar_layout = QtWidgets.QGridLayout()
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '水平数^因素数  ')
        self.search_icon.setFont(qtawesome.font('fa', 20))
        self.search_icon.setStyleSheet('''
            QLabel{
                margin-top: 40px;
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
                    font-family: SimHei;
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
                font-family: SimHei;
            }
        ''')
        self.output_box.setStyleSheet('''
           QPlainTextEdit{
               border:3px solid gray;
               height: 50px;
               border-radius:5px;
               padding 5px;
               font-size: 25px;
               font-family: SimHei;
           }
        ''')

        self.factor_box_label = QtWidgets.QLabel("水平因素框")
        self.factor_box_label.setStyleSheet('''
            QLabel {
                font-family: SimHei;
                font-size: 30px;
            }
        ''')
        self.output_box_label = QtWidgets.QLabel("样例生成框")
        self.output_box_label.setStyleSheet('''
            QLabel {
                font-family: SimHei;
                font-size: 30px;
            }
        ''')
        self.commit_button = QtWidgets.QPushButton("生成测试用例")
        self.commit_button.setObjectName("generate_button")
        self.commit_button.setStyleSheet('''
            QPushButton#generate_button{
                width: 30px;
                height: 40px;
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: SimSun;
                font-size: 30px;
            }
            QPushButton#generate_button:hover{
                width: 30px;
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Arial;
                font-family: SimSun;
            }
            QPushButton#generate_button:pressed{
                width: 30px;
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Arial;
                font-family: SimSun;
            }
        ''')

        self.reset_button = QtWidgets.QPushButton("重置")
        self.reset_button.setObjectName("reset_button")
        self.reset_button.setStyleSheet('''
                    QPushButton#reset_button{
                        width: 30px;
                        height: 40px;
                        background-color: gray;
                        border: 3px solid gray;
                        border-radius: 5px;
                        color: white;
                        font-family: SimSun;
                        font-size: 30px;
                    }
                    QPushButton#reset_button:hover{
                        width: 30px;
                        background-color: rgb(65,65,65);
                        border: 3px solid gray;
                        border-radius: 5px;
                        border-color: rgb(65,65,65);
                        color: white;
                        font-family: Arial;
                        font-family: SimSun;
                    }
                    QPushButton#reset_button:pressed{
                        width: 30px;
                        background-color: rgb(1,1,1);
                        border: 3px solid gray;
                        border-radius: 5px;
                        border-color: rgb(1,1,1);
                        color: white;
                        font-family: Arial;
                        font-family: SimSun;
                    }
                ''')

        self.commit_button.clicked.connect(self.on_commit_factor_num)
        self.reset_button.clicked.connect(self.on_button_reset_input_box)
        self.right_bar_layout.addWidget(self.search_icon, 1, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_search_widget_input, 1, 1, 1, 5)
        self.right_bar_layout.addWidget(self.factor_box_label, 2, 0, 1, 1)
        self.right_bar_layout.addWidget(self.output_box_label, 2, 3, 1, 1)
        self.right_bar_layout.addWidget(self.factor_box, 3, 0, 3, 3)
        self.right_bar_layout.addWidget(self.output_box, 3, 3, 3, 4)
        self.right_layout.addWidget(self.commit_button, 6, 1, 1, 3)
        self.right_layout.addWidget(self.reset_button, 6, 5, 1, 3)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)
        self.right_bar_widget.setVisible(False)
        self.commit_button.setVisible(False)
        self.reset_button.setVisible(False)

    def on_button_generating_table_page_switch(self):
        self.right_bar_widget.setVisible(True)
        self.commit_button.setVisible(True)
        self.reset_button.setVisible(True)
        self.title_widget.setVisible(False)
        self.right_subwidgets.setVisible(False)

    def on_button_main_page_switch(self):
        self.right_bar_widget.setVisible(False)
        self.commit_button.setVisible(False)
        self.reset_button.setVisible(False)
        self.right_subwidgets.setVisible(True)
        self.title_widget.setVisible(True)

    def on_button_reset_input_box(self):
        self.factor_box.setPlainText("")
        self.output_box.setPlainText("")
        self.right_search_widget_input.setText("")

    def error_msg_box(self):
        self.error_msgbox = QtWidgets.QMessageBox()
        self.error_msgbox.setWindowTitle("错误")
        self.error_msgbox.setText("输入格式有误，请重新输入！！")
        confirm_button = QtWidgets.QPushButton("确定")
        cancle_button = QtWidgets.QPushButton("取消")
        confirm_button.setStyleSheet('''
            QPushButton{
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: SimSun;
                font-size:25px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Arial;
                font-family: SimSun;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Arial;
                font-family: SimSun;
            }
        ''')
        cancle_button.setStyleSheet('''
            QPushButton{
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: SimSun;
                font-size:25px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Arial;
                font-family: SimSun;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Arial;
                font-family: SimSun;
            }
        ''')
        self.error_msgbox.addButton(confirm_button, QtWidgets.QMessageBox.YesRole)
        self.error_msgbox.addButton(cancle_button, QtWidgets.QMessageBox.NoRole)
        self.error_msgbox.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.error_msgbox.setStyleSheet('''
            QMessageBox{
                font-family:SimHei;
                font-size:25px;
                background-color:white;
                border:5px solid gray;
                border-radius:10px;
            }
        ''')
        self.error_msgbox.exec_()
        if self.error_msgbox == QtWidgets.QMessageBox.Ok:
            self.factor_box.setPlainText("")
            self.output_box.setPlainText("")
            self.right_search_widget_input.setText("")
        elif self.error_msgbox == QtWidgets.QMessageBox.Cancel:
            self.factor_box.setPlainText("")
            self.output_box.setPlainText("")
            self.right_search_widget_input.setText("")
            return

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
                font-family: SimSun;
                font-size:25px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Arial;
                font-family: SimSun;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Arial;
                font-family: SimSun;
            }
        ''')
        cancle_button.setStyleSheet('''
            QPushButton{
                background-color: gray;
                border: 3px solid gray;
                border-radius: 5px;
                color: white;
                font-family: SimSun;
                font-size:25px;
            }
            QPushButton:hover{
                background-color: rgb(65,65,65);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(65,65,65);
                color: white;
                font-family: Arial;
                font-family: SimSun;
            }
            QPushButton:pressed{
                background-color: rgb(1,1,1);
                border: 3px solid gray;
                border-radius: 5px;
                border-color: rgb(1,1,1);
                color: white;
                font-family: Arial;
                font-family: SimSun;
            }
        ''')
        self.empty_msgbox.addButton(confirm_button, QtWidgets.QMessageBox.YesRole)
        self.empty_msgbox.addButton(cancle_button, QtWidgets.QMessageBox.NoRole)
        self.empty_msgbox.setStyleSheet('''
            QMessageBox{
                font-family:SimHei;
                font-size:25px;
                background-color:white;
                border:5px solid gray;
                border-radius:10px;
            }
        ''')
        self.empty_msgbox.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.empty_msgbox.exec_()
        if self.empty_msgbox == QtWidgets.QMessageBox.Yes:
            self.factor_box.setPlainText("")
            self.output_box.setPlainText("")
            self.right_search_widget_input.setText("")
        elif self.empty_msgbox == QtWidgets.QMessageBox.Cancel:
            self.factor_box.setPlainText("")
            self.output_box.setPlainText("")
            self.right_search_widget_input.setText("")
            return

    @staticmethod
    def find_factor_num_in_table(factor_num_str, table):
        result = []
        input_level_num = int(factor_num_str.split('^')[0])
        input_factor_num = int(factor_num_str.split('^')[1])
        for index, line in enumerate(table):
            if '^' in line:
                table_len = line.split(' ')[-1].split('\n')[0]
                table_len = int(table_len.split('n=')[-1])
                table_factor_num = line.split(' ')[0]
                level_num = int(table_factor_num.split('^')[0])
                factor_num = int(table_factor_num.split('^')[1])
                if input_level_num == level_num and input_factor_num == factor_num:
                    for i in range(index + 1, index + table_len + 1):
                        result.append(table[i].split('\n')[0])
                    break
        return result

    def on_commit_factor_num(self):
        self.factor_num = self.right_search_widget_input.text()
        self.factor_level = self.factor_box.toPlainText()
        if '^' in self.factor_num:
            if self.factor_level is '':
                self.empty_msg_box()
                return
            table = Tools.get_normal_table()
            result = MainUI.find_factor_num_in_table(self.factor_num, table)
            sample_list = []
            factor_list = []
            outputs = []
            final_result = ""
            for sample in result:
                sample_list.append([int(x) for x in sample])
            self.factor_level = self.factor_box.toPlainText()
            self.factor_level = re.split("\n", self.factor_level)
            for factor in self.factor_level:
                factor_list.append(factor.split(','))
            # print(sample_list)
            # print(factor_list)

            for samle in sample_list:
                output = []
                for i, index in enumerate(samle):
                    output.append(factor_list[i][index])
                outputs.append(output)
            for _result in outputs:
                for i, __result in enumerate(_result):
                    if i == len(_result) - 1:
                        final_result += (__result + "\n")
                    final_result += (__result + ",")
            self.output_box.setPlainText(final_result)
        else:
            self.error_msg_box()


class Tools:
    def __init__(self):
        self.table = []
        self.lines = []

    def get_table(self):
        with open("./data/ts723_Designs.txt", "r") as f:
            self.lines = f.readlines()
        return self.lines
    @staticmethod
    def get_normal_table():
        with open("./data/ts723_Designs.txt", "r") as f:
            lines = f.readlines()
        return lines[:157]
