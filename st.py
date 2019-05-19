#class 類別
class Student:
    def __init__(self, name):#初始化
        self.name = name
        self.do_hw()
        self.study()
        self.sleep()
        print('我誕生了')

    def do_hw(self):
        print('我在做作業~')

    def study(self):
        print('我在讀書...')

    def sleep(self):
        print('終於能睡覺了...')
s = Student('zero')
print(s.name)    