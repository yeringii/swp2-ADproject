from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from button import *
from mainWindow import *


# 사용자 정보 입력 창
class UserInfoWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.vbox = QVBoxLayout()

        #배경설정
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(),Qt.white)
        self.setPalette(p)

        # 정보를 입력하라는 라벨
        self.inputMessageLabel = QLabel()
        self.inputMessageLabel.setText('사용자 정보를 입력하세요')
        self.hbox1.addWidget(self.inputMessageLabel)

        # 이름 입력 칸
        self.nameLabel = QLabel()
        self.nameLabel.setText('이름')
        self.nameInputEdit = QLineEdit()
        self.hbox2.addWidget(self.nameLabel)
        self.hbox2.addWidget(self.nameInputEdit)

        # 몸무게 입력 칸
        self.weightLabel = QLabel()
        self.weightLabel.setText('몸무게')
        self.weightInputEdit = QLineEdit()
        self.hbox3.addWidget(self.weightLabel)
        self.hbox3.addWidget(self.weightInputEdit)

        # 이름과 몸무게를 입력하고 누르면 다음 창으로 넘어감
        self.completeButton = Button('완료', self.completeButtonClicked)
        self.hbox4.addWidget(self.completeButton, alignment=Qt.AlignBottom)

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.setLayout(self.vbox)

        self.setGeometry(400, 400, 250, 400)
        self.setWindowTitle('Water Intake Alert')
        self.setWindowIcon(QIcon('waterdrop.png'))

    # 완료 버튼을 누르면 사용자가 입력한 정보 (이름, 몸무게)를 다음 창 객체에게 넘기고 소멸

    def completeButtonClicked(self):
        name = self.nameInputEdit.text()
        weight = self.weightInputEdit.text()
        self.nextWindow = MainWindow(name, int(weight))
        self.nextWindow.show()
        self.close()