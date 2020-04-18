'''
Running median
'''

import math

def runningMedian(arr):
    print('%.1f' % arr[0])
    arr.pop(0)
    for x in range(len(arr)):
        temp = arr[0:(x+1)]
        temp.sort()
        if len(temp) % 2 == 0:
            i1 = int(len(temp)/2)
            i2 = int(i1-1)
            median = float((temp[i1]+temp[i2])/2)
        else:
            i = math.floor(len(temp)/2)
            median = float(temp[i])
        print('%.1f' % median)        

input = [6,12,4,5,3,8,7]

runningMedian(input)
