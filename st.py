#class 類別
class Student:
    def __init__(self, name, score):#初始化
        self.name = name
        self.score = score
        print('我誕生了')

    def do_hw(self, hw):
        print('我在做作業~', hw)

    def study(self):
        print('我在讀書...')
        self.score += 5

    def sleep(self):
        print('終於能睡覺了...')
s1 = Student('zero', 100)
s2 = Student('sky', 95)
print(s1.name, s1.score) 
print(s2.name, s2.score)

s2.study()
print(s2.name, s2.score)  