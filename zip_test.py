#zip 使用
a = [1,2,3]
b = [4,5,6]
ab = zip(a, b)
print(list(ab)) #加list來可視化此結果
for i, j in zip(a, b):
    print(i / 2 , j * 2)