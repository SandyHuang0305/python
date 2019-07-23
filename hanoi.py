#漢諾塔
count = 0
def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print('{}:{}-->'.format(1, src, dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst) #A柱搬到B柱
        print('{}:{}-->{}'.format(n, src, dst))
        count += 1
        hanoi(n-1, mid, dst, src) #B柱搬到C柱
hanoi(3, 'A', 'C', 'B')
print(count)
