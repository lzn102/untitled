import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from GUI框架测试 import untitled


class Untitled(QMainWindow, untitled.Ui_ToolBox):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Untitled()

    win.show()
    sys.exit(app.exec())