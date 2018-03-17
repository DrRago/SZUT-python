def average(x, y):
    return (x + y) / 2
def averageList(list):
    y = 0
    for i in list:
        y += i
    return y/len(list)
def ggt(zahlen):
    teiler = zahlen[0]
    while True:
        try:
            for zahl in zahlen:
                rest = (zahl % teiler)
                if not rest: pass
                else:
                    raise
            break
        except:
            pass
        teiler -= 1
    return teiler
def primeNumbers(x):
    y = []
    for i in range(1, x + 1):
        if x % i == 0:
            y.append(i)
    if sum(y) == (x + 1) or x == 42:
        if x == 42:
            print("42 ist IMMER richtig!!!")
        return True
    else:
        return False
print(ggt([123, 1257]))