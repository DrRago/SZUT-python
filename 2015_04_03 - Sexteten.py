def sexToDez(sexList):
    # Funktion zum Umrechnen von einer Sextetenzahl in eine Dezimalzahl als Integer
    sexteten = {"<": 0, ">": 1, "*": 2, "+": 3, "(": 4, ")": 5}
    hex = ""
    for i in sexList:
        hex += str(sexteten[i])
    list = [i for i in str(hex)]
    list.reverse()
    count = 0
    res = 0
    for i in list:
        res += (6 ** count) * int(i)
        count += 1
    return res


def dezToSex(dez):
    # Funktion zum Umrechnen einer Dezimalzahl in eine Sextetenzahl als String
    sexteten = {0: "<", 1: ">", 2: "*", 3: "+", 4: "(", 5: ")"}
    res = []
    sex = ""
    while dez > 0:
        a = int(dez % 6)
        dez = (dez - a) / 6
        res.append(a)
    res.reverse()
    for i in res:
        sex += str(sexteten[i])
    return sex


def writeFile(toWrite):
    # Funktion zum Schreiben der Lösungsdatei
    spacelist.append(len(dezToSex(dez)))
    maxspaces = max(spacelist)
    sexstr = dezToSex(dez)
    for i in range(0, len(writelist), 2):
        toWrite = toWrite + " " + ((maxspaces - (len(str(writelist[i])))) * " ") + str(writelist[i]) + " | " + ((maxspaces - (len(str(writelist[i + 1])))) * " ") + str(writelist[i + 1]) + "\n"
    w.write(toWrite)
    result =((maxspaces - (len(sexstr))) * " ") + sexstr + " | " + ((maxspaces - (len(str(dez)))) * " ") + str(dez)
    w.write("-" + (len(result) - len(str(dez)) - 4) * "-" + " | " + ((len(result) - len(sexstr) - 3) * "-") + "\n")
    w.write(" " + result)
# Definieren Verschiedener Variablen
result = ""
readLine = []
sexList = []
sexstr = ""
dez = 0
toWrite = ""
spacelist = []
dezspacelist = []
writelist = []

if __name__ == "__main__":
    try:
        f = open("Aufgabe.txt", "r")  # Öffnen der Aufgabendatei
    except:
        print("Es ist ein Fehler beim Öffnen der Aufgabendatei aufgetreten,\nüberprüfen Sie ihren Pfad und versuchen Sie es erneut")  # Außnahme bei einem Fehler
    try:
        w = open("Loesung.txt", "w")  # Öffnen der Lösungsdatei
    except:
        print("Es ist ein Fehler beim Schreiben der Lösungsdatei aufgetreten,\nüberprüfen Sie ihren Pfad und versuchen Sie es erneut")  # Außnahme bei einem Fehler
    for line in f:
        readLine = [i for i in str(line)]  # Lesen der Aufgabendatei Zeilenweise
        for i in range(len(line)):
            if readLine[i] == " " or readLine[i] == "" or readLine[i] == "-" or readLine[i] == "\n":  # Aussortieren von Unnötigen Zeichen
                continue
            else:
                sexList.append(readLine[i])
        sexstr = "".join(map(str, sexList))  # Umwandeln der Liste mit den Sextetenzahlen in einen String
        spacelist.append(len(str(sexstr)))  # Speichern der Stelen der Sextetenzahlen in eine Liste
        dezspacelist.append(len(str(sexToDez(sexstr))))  # Speichern der Stellen der Dezimalzahlen in eine Liste
        writelist.append(sexstr)  # Speichern der einzelnen Sextetenzahlen in einer Liste
        writelist.append(sexToDez(sexstr))  # Speichern der einzelnen Dezimalzahlen in einer Liste
        dez += sexToDez(sexstr)  # Aufsummieren der Dezimalzahlen für das Ergebnis
        sexList.clear()
    writeFile(toWrite)  # Aufrufen der Funktion zum Schreiben der Lösungsdatei
    f.close()  # Schließen der Aufgabendatei
    w.close()  # Schließen der Lösungsdatei
    print("Fertig")
    input()