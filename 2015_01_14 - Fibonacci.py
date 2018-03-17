a = 0
b = 1
i = 0
while True:
    f = int(input("Bitte geben Sie die Zahlenmenge an: "))
    while i < f:
        c = a + b
        i += 1
        print(c)
        if i < f:
            a = b + c
            i += 1
            print(a)
            if i < f:
                b = a + c
                i += 1
                print(b)
            else:
                break
        else:
            break
    re = str(input("Wollen Sie neu starten?: "))
    if re == "Ja":
        continue
    else:
        break