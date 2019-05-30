#try 練習
try:
    file = open('ee.txt', 'r+')
except Exception as e:
    print(e)
    response = input('do you need to creat a new file?')
    if response == 'y':
        file = open('ee.txt', 'w')
    else:
        pass
else:
    file.write('我在這~')
    file.close()                