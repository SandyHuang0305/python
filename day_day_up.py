# 1% 的力量
dayup = pow(1.001, 365) # 每天努力1%
print(dayup)
print('----------------')
daydown = pow(0.999, 365)
print(daydown)

print('向上 : {:.2f}, 向下 : {:.2f}'.format(dayup, daydown))