__author__ = "Pascal de Vries & Leonhard Gahr"
__pythonVersion__ = "3.4.3"
__task__ = "Verschluesselungsaufagabe"
#-*- coding:cp1252 -*-
import zlib
import random
import argparse
import os
from time import clock
 
def myEncoding(sourcefile, destfile, password):
    """"Diese Funktion Verschluesselt eine Datei eines beliebien Formats. Sie gibt eine Datei mit dem Format cip aus. Sie benötigt die Parameter [sourcefile], [destfile] und [password]"""
    times = clock()
    byteCounter = 1
    percentlist = [0, 100]
    filesize = os.path.getsize(sourcefile)
    print("average time untli finish:", round(filesize / 116508.444), "seconds")
    print("0 % finnished")
    count = 0 #Gibt an welxches Zeichen von password genutzt werden soll
    with open(sourcefile, "rb") as source: #die zu verschlüsselnde Datei wird binär eingelesen
        with open(destfile, "wb") as dest: #die Zieldatei wird zum binären Schreiben geöffnet
            ending = sourcefile.rsplit(".")[-1] #die Dateiendung wird ermittelt
            dest.write(b"cip" + bytes(str(len(ending)), "utf8") +  bytes(ending, "utf8")) # der header wird erstellt
            checkSum = abs(zlib.crc32(bytes(password, "utf8"))) #die crc32 Checksumme wird mit hilfe des Passworts gebildet
            checkSum = bin(checkSum)[2:] #die Checksumme wird binär umgewandelt und das '0b' wird abgetrennt
            while len(checkSum) < 32: #die Checksumme wird mit 0 aufgefüllt bis sie 32 Zeichen hat
                checkSum = "0" + checkSum
            Z3 = checkSum[0:8] #die Checksumme wir in vier acht-bit Zahlen aufgeteilt
            Z2 = checkSum[8:16]
            Z1 = checkSum[16:24]
            Z0 = checkSum[24:32]
            random.seed(int((Z2 + Z1 + Z0), 2)) #der Randomgenerator wird mit drei der Checksumme Zahlen gefeedet
            readByte = source.read(1) #readByte wir ein byte von der zu Verschlüsselnden Datei zugewiesen
            while readByte != b"": #die Schleife läuft so lange readByte ein Zeichen enthält
                dest.write(bytes([(int.from_bytes(readByte, "big") + int(Z3, 2) + random.randint(0, 255) + int.from_bytes(bytes(password[count], "utf8"), "big")) % 256])) #das zeichen wird codiert und in die Zeildatei geschrieben
                if count <= len(password) - 2: #Die zu verwendende Stelle des Passwordes wir festgelegt
                    count += 1
                else: #ist das Password komplett genutzt worden, wird es wieder auf Stelle 0 zurückgesetzt
                    count = 0
                percentage = round(byteCounter / filesize * 100)
                if percentage not in percentlist:
                    print(int(percentage), "% finnished")
                    percentlist.append(percentage)
                byteCounter += 1
                readByte = source.read(1) #das nächste zeichen wird festgelegt
    times = round(clock() - times)
    if times > 60:
        print("Encrytion finnished without errors in", int(times / 60), "minutes", "and",  int(times % 60), "seconds")
    else:
        print("Encryption finnished without errors in", times, "seconds") #ifnormation für den Benutzer über die fertigstellung des Vorgangs
 
def myDecoding(sourcefile, destfile, password):
    """Diese Funktion Entschlüsselt eine Datei des Formats cip. Sie benötigt die Parameter [sourcefile], [destfile] und [password]"""
    times = clock()
    byteCounter = 1
    percentlist = [0, 100]
    filesize = os.path.getsize(sourcefile)
    print("0 % finnished")
    count = 0 #Gibt an welches Zeichen von password genutzt werden soll
    with open(sourcefile, "rb") as source: # die zu Entschlüsselnde Datei wir zum binären-lesen geöffnet
        if not source.read(3) == b"cip": #es wird geprüft ob die zu entschlüsselnde Datei eine .cip Datei ist
            print("That file isn't supported") #ist die Datei nicht .cip wird ein fehler ausgegeben
        else: #ist die Datei .cip wird das Programm normal weiter geführt
            endinglenght = int(source.read(1)) #die Länge der ursprünglichen Datei wird ermittelt
            ending = source.read(endinglenght) #die ursprüngliche Dateiendung wird ermittelt
            destfile += "." + ending.decode("utf8") #die Zieldatei wird mit der Endung versehen
            with open(destfile, "wb") as dest: #die Zieldatei wird zum binären-schreiben geöffner
                checkSum = abs(zlib.crc32(bytes(password, "utf8"))) #die crc32 Checksumme wird mit hilfe von password gebildet
                checkSum = bin(checkSum)[2:] #die Checksumme wird binär umgewandelt und das '0b' wird abgetrennt
                while len(checkSum) < 32: #die Checksumme wird mit 0 aufgefüllt bis sie 32 Zeichen hat
                    checkSum = "0" + checkSum
                Z3 = checkSum[0:8] #die Checksumme wir in vier acht-bit Zahlen aufgeteilt
                Z2 = checkSum[8:16]
                Z1 = checkSum[16:24]
                Z0 = checkSum[24:32]
                random.seed(int((Z2 + Z1 + Z0), 2)) #der Randomgenerator wird mit drei der Checksumme Zahlen gefeedet
                readByte = source.read(1) #readByte wir ein byte von der zu Verschlüsselnden Datei zugewiesen
                while readByte != b"": #die Schleife läuft so lange readByte ein Zeichen enthält
                    dest.write(bytes([(int.from_bytes(readByte, "big") - int(Z3, 2) - random.randint(0, 255) - int.from_bytes(bytes(password[count], "utf8"), "big")) % 256]))  #das zeichen wird decodiert und in die Zeildatei geschrieben
                    if count <= len(password) - 2: #Die zu verwendende Stelle des Passwordes wir festgelegt
                        count += 1
                    else: #ist das Password komplett genutzt worden, wird es wieder auf Stelle 0 zurückgesetzt
                        count = 0
                    percentage = round(byteCounter / filesize * 100)
                    if percentage not in percentlist:
                        print(int(percentage), "% finnished")
                        percentlist.append(percentage)
                    byteCounter += 1
                    readByte = source.read(1)
    times = round(clock() - times)
    if times > 60:
        print("Encrytion finnished without errors in", int(times / 60), "minutes", "and",  int(times % 60), "seconds")
    else:
        print("Encryption finnished without errors in", times, "seconds")
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #Hinzufügen von argparse-Argumenten
    parser.add_argument("-c", "--cipher", action = "store_true", dest = "c", help = "use this argument to encrypt a file")
    parser.add_argument("-d", "--decipher", action = "store_true", dest = "d", help = "use this argument to decrypt a file")
    parser.add_argument("-p", "--password", required = True, type = str, dest = "password", help = "this is a reqiured argument. Type your password here")
    parser.add_argument("-i", "--inputfile", required = True, type = str, dest = "sourcefile", help = "this is a required argument. Type your inputfile here")
    parser.add_argument("-o", "--outputfile", type = str, default = "default", dest = "destfile", help = "use that optional argument to set your outputfile. The file is always: [your input].cip")
    args = parser.parse_args()
 
    if args.destfile == "default" and args.c == True: #es wird geprüft ob eine Zieldatei angegeben wurde und ob ver- oder entschlüsselt werden soll
        args.destfile = args.sourcefile.rsplit(".", 1)[0] + ".cip" #ein Zieldateiname wird angelegt, da keiner vorhanden ist
    elif args.destfile == "default" and args.d == True: #es wird geprüft ob eine Zieldatei angegeben wurde und ob ver- oder entschlüsselt werden soll
        args.destfile = args.sourcefile.rsplit(".", 1)[0] #ein Zieldateiname wird angelegt, da keiner vorhanden ist
 
    if not os.path.isfile(args.sourcefile): #es wird überpräft ob die Quelldatei existiert
        raise FileNotFoundError("Sourcefile does not Exist in that directory") #Ein fehler wird ausgegeben, wenn die datei nicht existiert
 
    if os.path.isfile(args.destfile): #es wird überpräft ob die Zeildatei existiert
        while True:
            g = input("destfile does already exist in that directory. Do you want to replace it?(Y/N)") #Eine Eingabe wird aufgefordert
            if g == "Y" or g == "y": #die Eingabe wird auf ihren Inhalt überprüft
                break
            elif g == "N" or g == "n":
                raise FileExistsError("destfile does already exist in that directory. Please change the directory") #will man die datei nicht ersetzten, wird ein Fehler ausgegeben
            else:
                print("Invalid input")
 
    if args.c == True and args.d == False: #es wird überprüft ob verschlüsselt werden soll
        myEncoding(args.sourcefile, args.destfile, args.password) #verschlüsselungsfunktion wird aufgerufen
    elif args.d == True and args.c == False: #es wird überprüft ob entschlüsselt werden soll
        myDecoding(args.sourcefile, args.destfile, args.password) #entschlüsselungsfunktion wird aufgerufen
    elif args.c == False and args.d == False: #Es wird überprüft, ob keine der Argumente zum ent- oder verschlüsseln angegeben wurden
        raise TypeError("One of the following arguments are required: -c/--cipher, -d/--decipher") #ein fehler wird ausgegeben
    elif args.c == True and args.d == True: #es wird überprüft, ob beide der Argumente zum ent- oder verschlüsseln angegeben wurden
        raise TypeError("Only one of the following arguments is allowed: -c/--cipher, -d/--decipher") #ein fehler wird ausgegeben