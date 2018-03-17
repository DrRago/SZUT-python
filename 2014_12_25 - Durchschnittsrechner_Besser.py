# -*- coding: iso-8859-1 -*-
# Variablen werden Definiert
diagramm = " Diagramm:\n"
sum = 0
count = 0
print(" Durchschnittsrechner:")  #Programmtitel wird ausgegeben
while True:
    try:
        number = float(input(" Bitte Wert eingeben(<0  beendet): "))  #Die Eingabe des Wertes wird aufgefordert
    except:
        print(" Bitte geben Sie eine Zahl an!")
        continue
    if number >= 99999999:
        print(" Ihre Zahl ist zu groß!")
    elif number >= 0:  #Bedingung zum beenden des Programms wird abgefragt
        sum += number  #Die eingegebenen Zahlen werden aufaddiert
        count += 1  #Anzahl der Eingegebenen Zahlen wird festgehalten
        diagramm += (" " + "#" * round(number)) + "\n"  #Das Diagramm wird gespeichert
    elif count == 0:
            print(" Es müssen noch zwei Werte angegeben werden")
    elif count == 1:
                print(" Es muss noch ein Wert angegeben werden")
    else:
        break

print(diagramm, "Sie haben", count, "Zahlen eingegeben und der Durchscnitt beträgt:", round(sum / count, 3))  # Das Ergebnis wird ausgegeben