while True:
    function = input('Geben Sie Ihre gewünschte Funktion an ("?" für nähere Informationen): ')  # Funktionsauswahl wird aufgefordert
    if function == "1":
        liststr = 0
        c = 0
        divisor = []
        num = int(input("Bitte geben Sie eine Zahl an: "))  # Die Zahl, zu der die Teiler ermittelt werden soll, wird abgefragt
        for i in range(1, num):
            if num % i == 0:  # Teiler werden mithilfe von Modulu ermittelt
                c += 1  # Zähler zur ermittlung der Teilermenge wird hochgezählt
                divisor.append(i)  # Teiler wird einer Liste hinzugefügt
        liststr = ', '.join(map(str, divisor))  # Die Liste wird in einen String dupliziert
        if liststr == "":
            liststr = "None"
        print("Die Zahl", num, "hat", c, "Teiler:", liststr)  # Die Teiler und die Teilermenge wird ausgegeben
    elif function == "2":
        c1 = 0
        c2 = 0
        num = int(input("Bitte geben Sie eine Zahl an: "))  # Zahl du der ein Freund gefunden werden soll wird abgefragt
        for i in range(1, num):
            if num % i == 0:
                c1 += i  # Die Teilf(x) = x³er der Zahl werden ermittelt und zusammengezählt
        for i in range(1, c1):
            if c1 % i == 0:
                c2 += i  # Die Teiler der Summe der Teiler der anfangszahl werden ermittelt und zusaammengezält
        if c2 == num:  # Überprüfung ob die zweite Teilersumme der anfangszahl entspricht
            if c2 < c1:
                print(c2, "und", c1, "sind befreundet")  # Ausgabe der befreundeten Zahlen(Der größe nach sortiert)
            elif c2 > c1:
                print(c1, "und", c2, "sind befreundet")  # Ausgabe der befreundeten Zahlen(Der größe nach sortiert)
        else:
            print("None")
    elif function == "3":
        check = 0
        while check == 0:
            try:
                inputI = int(input("Bitte die Grenze eingeben: "))  # Obergrenze wird abgefragt
                if inputI >= 5000:
                    hint = input("Zu hohe Zahlen nehmen entsprechend Zeit in anspruch!\nMöchten Sie wirklich fortfahren? (1 für Ja): ")  # Information zur länge der Zahl
                    if hint == "1":
                        check += 1
                    else:
                        continue
                else:
                    check += 1
            except:
                print("Sie heben keine Ganzzahl eingegeben!")
        if inputI < 6:
            print("None\nFertig!")
        else:
            inputI += 1
            count = 0
            printed = []
            divsum = []
            for number in range(inputI):
                for i in range(1, number):
                    if number % i == 0:
                        count += i
                divsum.append(count)  # Die Summe der Teiler jeder Zahl wird in einer Liste gespeichert
                count = 0
            for i in range(1, inputI):
                for f in range(1, inputI):
                    if divsum[i] == f and divsum[f] == i and i != f and i not in printed and f not in printed:
                        print(i, "und", f, "sind befreundet")  # Ermittlung ob zwei Zahlen befreundet sind
                        printed.append(f and i)  # Zahlen zur Liste der ausgegebenen Zahlen hinzufügen
                    save = divsum[i]
                    if save == i and save != 0 and save not in printed:  # abfrage ob eine Zahl vollkommen ist
                        print(save, "ist vollkommen")  # vollkommene Zahl ausgeben
                        printed.append(save)  # Zahl zur Liste dder ausgegebenen Zahlen hinzufügen
            print("Fertig!")
    elif function == "0" or function == "exit":
        exit()  # Programm beenden
    elif function == "?":  # Informationen zu den Funktionen des Programms
        print('\nGeben Sie "1" ein um alle Teiler einer Zahl ermitteln zu lassen,')
        print('geben Sie "2" um den Freund einer Zahl ermitteln zu lassen,')
        print('geben Sie "3" ein um alle vollkommenen und befreundeten Zahlen zu ermitteln')
        print('oder geben Sie "0" / "exit" ein um zu beenden\n')
    else:
        print("Sie haben keine zugelassene Funktion ausgewählt, bitte versuchen Sie es erneut")