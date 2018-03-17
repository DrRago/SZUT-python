#Variablen werden Definiert
diagramm = "Diagramm:\n"
sum = 0
stop = 0
count = 0
print(" Durchschnittsrechner:")  #Programmtitel wird ausgegeben
while stop == 0:
    number = float(input(" Bitte Wert eingeben(<0  beendet): "))  #Die Eingabe des Wertes wird aufgefordert
    while number >= 0:  #Bedingung zum beenden des Programms wird abgefragt
        sum += number  #Die eingegebenen Zahlen werden aufaddiert
        count += 1  #Anzahl der Eingegebenen Zahlen wird festgehalten
        diagramm += (" " + "#" * round(number)) + "\n"  #Das Diagramm wird gespeichert
        break
    else:
        stop = 1
print(" Durchschnitt:", round(sum / count, 3), "\n", diagramm)  #Das Ergebnis wird ausgegeben
input("wait")
	