# coding: utf-8

import qtawesome
from PyQt5 import QtCore, QtWidgets

from gui_utils.custom_widgets import myQLineEdit


class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.setFixedSize(960, 700)
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
        # self.init_input_box()

    def init_button(self):
        self.left_close = QtWidgets.QPushButton("")
        self.left_visit = QtWidgets.QPushButton("")
        self.left_mini = QtWidgets.QPushButton("")
        self.left_close.setFixedSize(20, 20)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(20, 20)  # 设置按钮大小
        self.left_mini.setFixedSize(20, 20)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''
            QPushButton{ 
            background:#F76677;
            border-radius:10px;
            }
            QPushButton:hover{
            background:red;
            }
            ''')
        self.left_visit.setStyleSheet(
            '''
            QPushButton{
            background:#F7D674;
            border-radius:10px;
            
            }
            QPushButton:hover{
            background:yellow;
            }
        ''')
        self.left_mini.setStyleSheet(
            '''
            QPushButton{
                background:#6DDF6D;
                border-radius:10px;
            }
            QPushButton:hover{
                background:green;
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
        self.right_search_widget_input.setStyleSheet(
            '''
            QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }
            ''')
        # self.right_search_widget_input.returnPressed.connect(self.on_lineEdit_enter)

        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_search_widget_input, 0, 1, 1, 8)

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
        self.title_widget.setStyleSheet(
            '''
            QLabel#title_label {
                border:none;
                color: red;
                font-size:30px;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        '''
        )

        self.introduction_background = QtWidgets.QLabel()
        self.introduction_background.setObjectName("introduction_background")

        self.introduction_label_widget = QtWidgets.QLabel()
        self.introduction_label_widget.setObjectName("introduction_label")
        self.introduction_label_widget.setText(
            "本工具由1900301236谢浚霖开发，可以实现根据正交表以及输入的水平数和因素数自动生成测试用例\n\nPommesPeter\t\nEmail:me@pommespeter.com\t\nGithub ID: PommesPeter\t\nTencentQQ: 434596665")
        self.introduction_label_widget.setStyleSheet('''
            QLabel#introduction_label {
                border-radius:5px;
                font-size: 40px;
                font-family: " times new romance"
                background-color: gray;
            }
        ''')
        self.introduction_label_widget.wordWrap()
        self.introduction_label_widget.resize(50, 50)
        self.right_subwidgets_layout.addWidget(self.title_widget, 0, 1, 1, 8)
        self.right_subwidgets_layout.addWidget(self.introduction_label_widget, 0, 1, 1, 8)
        self.right_layout.addWidget(self.right_subwidgets, 0, 0, 1, 9)
        self.right_layout.addWidget(self.title_widget, 0, 0, 1, 10)

    def init_generating_table_page(self):
        self.right_bar_widget = QtWidgets.QFrame()
        # self.right_bar_widget = QtWidgets.QWidget()
        self.right_bar_layout = QtWidgets.QGridLayout()
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '水平数^因素数  ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_search_widget_input = QtWidgets.QLineEdit()
        self.right_search_widget_input.setPlaceholderText("请输入水平数^因素数")
        self.right_search_widget_input.setStyleSheet(
            '''
            QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }
            ''')

        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_search_widget_input, 0, 1, 1, 8)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)
        self.right_bar_widget.setVisible(False)

    def on_button_main_page_switch(self):
        self.right_bar_widget.setVisible(False)
        self.right_subwidgets.setVisible(True)

    def on_button_generating_table_page_switch(self):
        self.right_bar_widget.setVisible(True)
        self.right_subwidgets.setVisible(False)

    def on_lineEdit_enter(self):
        print(1)
        pass
