from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from button import *
from mainWindow import *
from user import *

import pickle
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt


# 메인 화면
class MainWindow(QWidget):

    def __init__(self, name, weight, parent=None):
        super().__init__(parent)
        self.user = User(name, weight)
        # pickle을 이용해서 사용자의 물 섭취량을 기록
        self.db = 'waterLog.pkl'
        self.waterLog = dict()

        #배경 설정
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(),Qt.white)
        self.setPalette(p)

        # 사용자의 수분 섭취량 정보에 대한 라벨
        self.titleText = QLabel()
        self.titleText.setText(f'{self.user.getName()}님의 금일 수분 섭취량')


        # 사용자의 수분 섭취량 표시
        # 텍스트 입력을 받지 못하게 setReadOnly(True)
        self.amountEdit = QTextEdit()
        self.amountEdit.setReadOnly(True)
        self.amountEdit.setText(f'0 / {self.user.getNeededWater()}')

        # 수분 섭취 기록 버튼
        # 누르면 사용자 객체에 오늘 마신 섭취량이 더해짐
        self.button_100ml = Button('100ml', self.buttonClicked)
        self.button_150ml = Button('150ml', self.buttonClicked)
        self.button_200ml = Button('200ml', self.buttonClicked)
        self.button_250ml = Button('250ml', self.buttonClicked)
        self.button_350ml = Button('350ml', self.buttonClicked)
        self.button_500ml = Button('500ml', self.buttonClicked)

        # 원한다면 시간대 별로 섭취량 총합을 그래프로 볼 수 있음
        self.graphButton = Button('통계 보기', self.showGraph)

        self.hbox1 = QHBoxLayout()
        self.hbox1.addWidget(self.titleText)

        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(self.amountEdit)

        self.hbox3 = QHBoxLayout()
        self.hbox3.addWidget(self.button_100ml)
        self.hbox3.addWidget(self.button_150ml)
        self.hbox3.addWidget(self.button_200ml)
        self.hbox3.addWidget(self.button_250ml)
        self.hbox3.addWidget(self.button_350ml)
        self.hbox3.addWidget(self.button_500ml)

        self.hbox4 = QHBoxLayout()
        self.hbox4.addWidget(self.graphButton)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.setLayout(self.vbox)

        self.setGeometry(400, 400, 250, 400)
        self.setWindowTitle('Water Intake Alert')
        self.setWindowIcon(QIcon('waterdrop.png'))


    # 버튼이 눌렸을 때의 객체 행동 정의
    def buttonClicked(self):
        key = self.sender().text()

        if key == '100ml':
            # datetime 모듈로 현재 시간을 얻어와서 섭취량과 함께 기록
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.user.drink(100)
            self.amountEdit.setText(
                f'{self.user.getWaterIntake()} / {self.user.getNeededWater()}')
            self.waterLog[now] = self.user.getWaterIntake()
            self.writeWaterLog()

        elif key == '150ml':
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.user.drink(150)
            self.amountEdit.setText(
                f'{self.user.getWaterIntake()} / {self.user.getNeededWater()}')
            self.waterLog[now] = self.user.getWaterIntake()
            self.writeWaterLog()

        elif key == '200ml':
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.user.drink(200)
            self.amountEdit.setText(
                f'{self.user.getWaterIntake()} / {self.user.getNeededWater()}')
            self.waterLog[now] = self.user.getWaterIntake()
            self.writeWaterLog()

        elif key == '250ml':
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.user.drink(250)
            self.amountEdit.setText(
                f'{self.user.getWaterIntake()} / {self.user.getNeededWater()}')
            self.waterLog[now] = self.user.getWaterIntake()
            self.writeWaterLog()

        elif key == '350ml':
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.user.drink(350)
            self.amountEdit.setText(
                f'{self.user.getWaterIntake()} / {self.user.getNeededWater()}')
            self.waterLog[now] = self.user.getWaterIntake()
            self.writeWaterLog()

        elif key == '500ml':
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.user.drink(500)
            self.amountEdit.setText(
                f'{self.user.getWaterIntake()} / {self.user.getNeededWater()}')
            self.waterLog[now] = self.user.getWaterIntake()
            self.writeWaterLog()

        else:
            pass

    # QWidget의 closeEvent Override
    # 이벤트가 종료될 때의 행동 정의
    def closeEvent(self, event):
        self.writeWaterLog()

    # pickle을 이용해서 바이너리 파일 읽기
    def readWaterLog(self):
        try:
            fH = open(self.db, 'rb')

        except FileNotFoundError as e:
            self.waterLog = dict()
            print(e)
            return self.waterLog

        try:
            self.waterLog = pickle.load(fH)

        except EOFError as e:
            self.waterLog = dict()
            print(e)
            return self.waterLog

        fH.close()

        return self.waterLog

    # pickle 모듈을 이용해서 파일을 열고, 섭취량을 기록
    def writeWaterLog(self):
        fH = open(self.db, 'wb')
        pickle.dump(self.waterLog, fH)
        fH.close()

    # 그래프 버튼을 누르면 사용자가 언제 얼마나 섭취해서 총 얼마나 마셨는지 알 수 있도록 그래프로 띄워줌
    def showGraph(self):
        logData = self.readWaterLog()
        X = np.array(list(logData.keys()))
        y = np.array(list(logData.values()))

        plt.plot(X, y, 'b-')

        plt.xlabel('Time')
        plt.ylabel('Water Intake')
        plt.title(r'Histogram of your Water Intake')

        plt.show()