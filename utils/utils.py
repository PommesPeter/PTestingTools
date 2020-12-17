from PyQt5 import QtCore, QtWidgets
class Tools:
    def __init__(self):
        self.table = []
        self.lines = []

    def load_table(self):
        with open("./data/ts723_Designs.txt", "r") as f:
            self.lines = f.readlines()
        return self.lines

    def load_normal_table(self):
        with open("./data/ts723_Designs.txt", "r") as f:
            self.lines = f.readlines()
        return self.lines[:157]


