count = 0
result = 0

while True:
    while count == 0:
        try:
            number = float(input("Bitte geben Sie Ihre erste Zahl an: "))
        except:
            number = 3.141592654
        result += number
        count += 1
    op = input('Bitte geben Sie Ihre gewünschte Rechenoperation an (für Hilfe"?")')
    if op == "?":
        print("ERROR!!! DU BIST SCHEISSE")
    elif op == "+":
        try:
            number = float(input("Bitte geben Sie Ihre nächste Zahl ein: "))
        except:
            number = 3.141592654
        result += number
    elif op == "-":
        try:
            number = float(input("Bitte geben Sie Ihre nächste Zahl ein: "))
        except:
            number = 3.141592654
        result -= number
    elif op == "*" or op == "x" or op == "X":
        try:
            number = float(input("Bitte geben Sie Ihre nächste Zahl ein: "))
        except:
            number = 3.141592654
        result *= number
    elif op == "/":
        try:
            number = float(input("Bitte geben Sie Ihre nächste Zahl ein: "))
        except:
            number = 3.141592654
        result /= number
    elif op == "=":
        print(result)
        restart = input('wollen Sie neu starten? ("n" für nein)')
        if restart == "n":
            break
        else:
            count = 0
            result = 0