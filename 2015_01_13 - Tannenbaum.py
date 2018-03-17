count = 0
counter = 0
while True:
    version = input("Bitte geben Sie die Programmversion an(a, b, c, d): ")
    if version == "a":
        try:
            count = int(input("Bitte geben Sie die Zeilenmenge an: "))
            for i in range(count):
                print(" "*(count-1-i)+"*"*(2*i+1))
        except:
            print("Ein unbekannter Fehler ist aufgetreten!")
    elif version == "b":
        try:
            count = int(input("Bitte geben Sie die Zeilenmenge an: "))
            for i in range(count):
                print(" " * (count - 1 - i) + "*" * (2 * i + 1))
            print((" " * (count - 1) + "*\n") * round(count / 3))
        except:
            print("Ein unbekannter Fehler ist aufgetreten!")
    elif version == "c":
        try:
            count = int(input("Bitte geben Sie die Zeilenmenge an: "))
            for i in range(count):
                print(" " * (count - 1 - i) + "*" * (2 * i + 1))
            print((" " * ((count-1) - (int(round(count / 5)/2))) + ("*" * round(count / 5)) + "*\n") * round(count / 3))
        except:
            print("Ein unbekannter Fehler ist aufgetreten!")
    elif version == "d":
        try:
            count = int(input("Bitte geben Sie die Zeilenmenge an: "))
            print(" " * (count) + "Y")
            for i in range(count):
                counter += 1
                if i % 2 == 1 and counter > 1:
                    print(" " * (count - 1 - i) + "I" + "*" * (2 * i + 1) + "I")
                else:
                    print(" " * (count - i) + "*" * (2 * i + 1))
            print((" " * ((count-1) - (int(round(count / 5)/2))) + ("*" * round(count / 5)) + "*\n") * round(count / 3))
        except:
            print("Ein unbekannter Fehler ist aufgetreten!")
    else:
        print("Sie haben eine nicht existierende Version angegeben!")
    restart = str(input("Wolen sie neustarten?(Ja/J für Ja und Nein/N für Nein): "))
    if restart == "Ja" or restart == "J" or restart == "j":
        count = 0
        counter = 0
    else:
        break