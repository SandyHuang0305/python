# 天天向上第三練習-有休息日的情況
dayup = 1.0
dayfactor = 0.01
for i in range (365):
    #有假日的情況-休息
    if i % 7 in [6, 0]:
        dayup = dayup * (1 - dayfactor)
    #工作日
    else:
        dayup = dayup * (1 + dayfactor)
print('工作日的力量: {:.2f}'.format(dayup))