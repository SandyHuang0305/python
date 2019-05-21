class Desk:
    def __init__(self, color):
        self.color = color
        print('我被製造出來了喔~')

    def re_color(self, new_color):
        self.color = new_color

d = Desk('blue')
d.re_color('red')
print(d.color)        
