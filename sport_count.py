from random import random

def printIntro():
    print('這個程式用於模擬選手A與B的比賽')
    print('程式運行需要A與B選手的能力值(以0-1之間的小數表示)')

def getInputs():
    a = eval(input('請輸入選手A的能力值:'))
    b = eval(input('請輸入選手B的能力值:'))
    n = eval(input('模擬比賽的場次:'))
    return a, b, n

def printSummary(winsA, winsB):
    n = winsA + winsB
    print('競賽分析開始, 共模擬{}場比賽'.format(n))
    print('選手A獲勝{}場比賽, 占比{:0.1%}'.format(winsA, winsA/n))
    print('選手B獲勝{}場比賽, 占比{:0.1%}'.format(winsB, winsB/n))

def gameOver(a, b):
    return a == 15 or b == 15
def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = 'A'
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = 'A'
    return scoreA, scoreB
    
def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

main()