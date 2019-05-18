#class 類別
class student:
    def _init_(self):#初始化
        print('我誕生了')

    def do_hw(self):
        print('我在做作業~')

    def study(self):
        print('我在讀書...')

    def sleep(self):
        print('終於能睡覺了...')
s = student()
s.do_hw()
s.study() 
s.sleep()       