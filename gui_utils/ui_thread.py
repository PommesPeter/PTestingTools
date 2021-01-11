import time

from PyQt5.QtCore import QThread, pyqtSignal


class UI_Thread(QThread):
    signal = pyqtSignal(str)

    def __init__(self):
        super(UI_Thread, self).__init__()

    def run(self):
        for i in range(100):
            self.signal.emit(str(i))
            time.sleep(1)
