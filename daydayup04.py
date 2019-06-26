#天天向上問題4
def dayUP(df): #dayfactor = df
    dayup = 1
    for i in range(365):
        #休息日
        if i % 7 in [6,0]: 
            dayup = dayup*(1 - 0.01)
        #工作日
        else: 
            dayup = dayup*(1 + df)
        return dayup  
dayfactor = 0.01
while  dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print('工作日的努力參數是:{:.3f}'.format(dayfactor))
print('hi')
print('hi2')    