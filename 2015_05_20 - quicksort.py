__author__ = 'Leonhard Gahr'

import random
myList = [random.randint(1, 100) for i in range(10)]

def qsort(myList):
    print(myList)
    if len(myList) <= 1:
        return myList
    else:
        if myList[0] > myList[-1] and myList[0] < myList[int(len(myList) / 2)]:
            pivot = myList[0]
        elif myList[-1] > myList[0] and myList[-1] < myList[int(len(myList) / 2)]:
            pivot = myList[-1]
        else:
            pivot = myList[int(len(myList) / 2)]
        print(pivot)
        return qsort([i for i in myList[pivot:] if i < pivot]) + [pivot] + qsort(i for i in myList if i >= pivot)

print(qsort(myList))