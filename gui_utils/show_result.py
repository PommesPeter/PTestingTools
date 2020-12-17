from PyQt5 import QtCore, QtWidgets


def load_table():
    with open("/home/pommespeter/workspace/Pwidgets/data/ts723_Designs.txt", 'r') as f:
        lines = f.readlines()
        print(lines)
    return lines



def find_normal_table(lines):
    for line in lines:
        pass
    pass


def find_mix_table():
    pass
