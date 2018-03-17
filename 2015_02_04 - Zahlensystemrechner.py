while True:
    bre = 0
    temp = 0
    dez = 0
    liste = []
    sysl = []
    div1 = 0
    count = 0
    num = 0
    sys = 0
    try:
        num = input("Bitte geben Sie Ihre Zahl ein: ")
    except:
        print("Sie haben keine Zahl angegeben")
    try:
        sys = int(input("Bitte geben Sie Ihr Startzahlensystem ein: "))
    except:
        print("Bitte geben Sie eine Zahl zwischen 2 und 16 an!")
        bre = 1
    syssl = [i for i in str(num)]
    for i in range(len(num)):
        if syssl[i] == " " or syssl[i] == "":
            continue
        else:
            sysl.append(syssl[i])
    for i in range(0, len(sysl)):
        int(i)
        if sysl[i] == "A" or sysl[i] == "a":
            sysl[i] = "10"
        elif sysl[i] == "B" or sysl[i] == "b":
            sysl[i] = "11"
        elif sysl[i] == "C" or sysl[i] == "c":
            sysl[i] = "12"
        elif sysl[i] == "D" or sysl[i] == "d":
            sysl[i] = "13"
        elif sysl[i] == "E" or sysl[i] == "e":
            sysl[i] = "14"
        elif sysl[i] == "F" or sysl[i] == "f":
            sysl[i] = "15"
    try:
        sysl = [int(i) for i in sysl]
    except:
        print("Sie haben ungültige Zeichen angegeben")
        bre = 1
    for i in sysl:
        if bre != 1 and i > sys - 1:
            print("Sie haben die Basis", sys, "überchritten")
            bre = 1
            break
    if bre != 1:
        if sys < 2 or sys > 17:
            print("Sie haben kein gültiges Zahlensystem angegeben!")
        else:
            sysl.reverse()
            for i in sysl:
                dez += (sys ** count) * int(i)
                count += 1
            temp = dez
            for i in range(2, 17):
                dez = temp
                while True:
                    div1 = int(dez / i)
                    toAppend = dez % i
                    if toAppend == 10:
                        toAppend = "A"
                    elif toAppend == 11:
                        toAppend = "B"
                    elif toAppend == 12:
                        toAppend = "C"
                    elif toAppend == 13:
                        toAppend = "D"
                    elif toAppend == 14:
                        toAppend = "E"
                    elif toAppend == 15:
                        toAppend = "F"
                    liste.append(toAppend)
                    dez = div1
                    if div1 == 0:
                        liste.reverse()
                        print(i, "er System:", ' '.join(map(str, liste)))
                        liste.clear()
                        break