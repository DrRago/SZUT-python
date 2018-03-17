def printFract(fract):
    print('/'.join(map(str, fract)), "=", round(fract[0] / fract[1], 4))


def inputFract():
    fract.append(int(input("Bitte geben Sie den Zähler ein: ")))
    fract.append(int(input("Bitte geben Sie den Nenner ein: ")))
    return fract


def ggT(fract):
    a = fract[0]
    b = fract[1]
    while b != 0:
        h = a % b
        a = b
        b = h
    return a


def cancelFract(fract):
    div = ggT(fract)
    fract[1] /= div
    fract[0] /= div
    return [int(i) for i in fract]


def negFract(fract):
    fract[0] *= -1
    return cancelFract(fract)


def invFract(fract):
    fract[0], fract[1] = fract[1], fract[0]
    return fract


def newFract():
    fract2.append(int(input("Bitte geben Sie den Zähler des zweiten Bruchs ein: ")))
    fract2.append(int(input("Bitte geben Sie den Nenner des zweiten Bruchs ein: ")))
    return fract2


def addFract(fract, fract2):
    fract[0] = fract[0] * fract2[1] + fract2[0] * fract[1]
    fract[1] *= fract2[1]
    return cancelFract(fract)


def subFract(fract, fract2):
    fract[0] = fract[0] * fract2[1] - fract2[0] * fract[1]
    fract[1] *= fract2[1]
    return cancelFract(fract)


def mulFract(fract, fract2):
    fract[0] *= fract2[0]
    fract[1] *= fract2[1]
    return cancelFract(fract)


def dicFract(fract, fract2):
    invFract(fract2)
    fract[0] *= fract2[0]
    fract[1] *= fract2[1]
    return cancelFract(fract)

if __name__ == "__main__":
    while True:
        fract2 = []
        fract = []
        try:
           fun = str(input("Funktion: "))
        except:
            print("Fehler, Falsche Eingabe!")
        if fun == "cancel":
            printFract(cancelFract(inputFract()))
        elif fun == "neg":
            printFract(negFract(inputFract()))
        elif fun == "inv":
            printFract(invFract(inputFract()))
        elif fun == "add":
            printFract(addFract(inputFract(), newFract()))
        elif fun == "sub":
            printFract(subFract(inputFract(), newFract()))
        elif fun == "mul":
            printFract(mulFract(inputFract(), newFract()))
        elif fun == "dic":
            printFract(dicFract(inputFract(), newFract()))
        elif fun == "exit":
            break
        else:
            print('Fehler, Falsche Eingabe!\n"cancel" zum kürzen\n"neg" zum negieren\n"inv" zum invertieren\n"add" zum addieren\n"sub" zum subtrahieren\n"mul" zum multiplizieren\n"dic" zum dividieren\n"exit" zum beenden')