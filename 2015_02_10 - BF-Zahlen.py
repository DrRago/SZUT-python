# Funktion zur ermittlung der Teilersumme einer Zahl
def divs(counter, i):
    divisor = []
    while counter < (i / 2) + 1:
        if i % counter == 0:
            divisor.append(counter)
        counter += 1
    return divisor
# Funktion zur Überprüfung zweier Zahlen auf ihre Freundschaft
def friend(divisor, i):
    s = sum(divisor)
    divisor = divs(1, s)
    if sum(divisor) == i and i not in printed and s not in printed:
        i = str(i) + " und " + str(s) + " sind befreundet"
        printed.append(s)
        printed.append(i)
        return i
    else:
        return None
if __name__ == "__main__":
    maxNumber = int(input("Bitte geben sie einen Endwert an: "))  # Obergrenze wird abgefragt
    if maxNumber <= 0:
        exit()
    printed = []
    for i in range(2, maxNumber + 1):  # for - Schleife zum Abfragen aller Zahlen
        c = 0
        if sum(divs(1, i)) == i:
            print(i, "ist vollkommen")
        else:
            s = friend(divs(1, i), i)
            if not s == None:
                print(s)