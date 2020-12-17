from PyQt5.QtCore import QThread, pyqtSignal


class UI_Thread(QThread):
    def __init__(self):
        super(UI_Thread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        pass
