from startWindow import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


# 메인 이벤트 루프를 함수로 정의
def main():
    import sys

    app = QApplication(sys.argv)
    startWindow = StartWindow()
    startWindow.show()
    #app.setWindowIcon(QIcon("waterdrop.png"))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()