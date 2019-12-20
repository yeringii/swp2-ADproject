# 사용자 정보를 담는 객체
class User:
    def __init__(self, name, weight):
        self.name = name
        self.neededWater = weight * 33
        self.waterIntake = 0

    def getName(self):
        return self.name

    def getNeededWater(self):
        try:
            str(self.neededWater)
        except:
            if str(self.waterIntake > self.neededWater):
                return
        return str(self.neededWater)

    def drink(self, amount):
        self.waterIntake += int(amount)

    def getWaterIntake(self):
        return str(self.waterIntake)