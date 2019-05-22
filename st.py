#class 類別
class Student:#class第一個字是大寫開頭
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

student = [s1, s2] 

for s in student:
    print(s.name, '的分數是', s.score)