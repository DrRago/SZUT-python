__author__ = "Pascal de Vries & Leonhard Gahr"
__pythonVersion__ = "3.4.3"
__task__ = "Verschlüsselungsaufagabe"

import zlib
import random
import argparse
import os
import time
import math
import getpass

class InputError(Exception):
    pass

class FileNotSupportedError(Exception):
    pass

def myEncoding(sourcefile, destfile, password):
    """"Diese Funktion Verschlüsselt eine Datei eines beliebien Formats. Sie gibt eine Datei mit dem Format cip aus. Sie benötigt die Parameter [sourcefile], [destfile] und [password]"""
    byteCounter = 1
    filesize = os.path.getsize(sourcefile)
    average = round(filesize / 29127.11111)

    if average == 0:
        print("Propably time until finnish: less than 1 second")
    else:
        if average > 60:
            if average / 60 >= 60:
                if average / 3600 >= 24:
                    if average / 86400 >= 7:
                        if average / 604800 >= 4:
                            if average / 2419200 >= 12:
                                if average / 29030400 >= 100:
                                    print("Propably time until finish:", int(average / 2903040000), "centuries,", int(average / 29030400 % 100), "years", int(average / 2419200 % 12), "months,", int(average / 604800 % 4), "weeks,", int(average / 86400 % 7), "days,", int(average / 3600 % 24), "hours,", int(average / 60 % 60), "minutes and", int(average % 60), "seconds")
                                else:
                                    print("Propably time until finish:", int(average / 29030400), "years,", int(average / 2419200 % 12), "months,", int(average / 604800 % 4), "weeks,", int(average / 86400 % 7), "days,", int(average / 3600 % 24), "hours,", int(average / 60 % 60), "minutes and", int(average % 60), "seconds")
                            else:
                                print("Propably time until finish:", int(average / 2419200), "months,", int(average / 604800 % 4), "weeks,", int(average / 86400 % 7), "days,", int(average / 3600 % 24), "hours,", int(average / 60 % 60), "minutes and", int(average % 60), "seconds")
                        else:
                            print("Propably time until finish:", int(average / 604800), "weeks,", int(average / 86400 % 7), "days", int(average / 3600 % 24), "hours,", int(average / 60 % 60), "minutes and", int(average % 60), "seconds")
                    else:
                        print("Propably time until finish:", int(average/ 86400), "days,", int(average / 3600 % 24), "hours,", int(average / 60 % 60), "minutes and", int(average % 60), "seconds")
                else:
                    print("Propably time until finish:", int(average / 3600), "hours,", int(average / 60 % 60), "minutes and", int(average % 60), "seconds" )
            else:
                print("Propably time until finish:", int(average / 60), "minutes and",  int(average % 60), "seconds")
        else:
            print("Propably time until finish:", average, "seconds")

    time.sleep(2)
    times = time.clock()

    if average <= 30:
        percentlist = [x for x in range(100) if not x % 20 == 0] + [100, 0]
    else:
        percentlist = [0, 100]

    print("00 % finnished")
    count = 0 

    with open(sourcefile, "rb") as source:
        with open(destfile, "wb") as dest:
            end = sourcefile.rsplit(".")[-1] 
            dest.write(b"cip" + bytes(str(len(end)), "utf8") +  bytes(end, "utf8"))
            checkSum = "%0.32d" %int(bin(abs(zlib.crc32(bytes(password, "utf8"))) )[2:])
            Z3 = checkSum[0:8]
            Z2 = checkSum[8:16]
            Z1 = checkSum[16:24]
            Z0 = checkSum[24:32]
            random.seed(int((Z2 + Z1 + Z0), 2)) 
            readByte = source.read(1) 

            while readByte != b"":
                dest.write(bytes([(int.from_bytes(readByte, "big") + int(Z3, 2) + random.randint(0, 255) + int.from_bytes(bytes(password[count], "utf8"), "big")) % 256])) 

                if count <= len(password) - 2:
                    count += 1
                else: 
                    count = 0

                percentage = math.floor(byteCounter / filesize * 100)

                if percentage not in percentlist:
                    if percentage % 5 == 0:
                        print("Aveage time left:", round(((time.clock() - times) * (100/percentage)) - (time.clock() - times)), "seconds")
                    print("%0.2d" %int(percentage), "% finnished")
                    percentlist.append(int(percentage))

                byteCounter += 1
                readByte = source.read(1) 
    times = round(time.clock() - times)

    if times == 0:
        print("The file", os.path.abspath(sourcefile), "was successfully encrypted as", os.path.abspath(destfile), "in less than 1 second")
    else:
        if times > 60:
            if times / 60 >= 60:
                if times / 3600 >= 24:
                    if times / 86400 >= 7:
                        if times / 604800 >= 4:
                            if times / 2419200 >= 12:
                                if times / 29030400 >= 100:
                                    print("The file", os.path.abspath(sourcefile), "was successfully encrypted as", os.path.abspath(destfile), "in\n" + str(int(times / 2903040000)), "centuries,", int(times / 29030400 % 100), "years", int(times / 2419200 % 12), "months,", int(times / 604800 % 4), "weeks,", int(times / 86400 % 7), "days,", int(times / 3600 % 24), "hours,", int(times / 60 % 60), "minutes and", int(times % 60), "seconds")
                                else:
                                    print("The file", os.path.abspath(sourcefile), "was successfully encrypted as", os.path.abspath(destfile), "in\n" + str(int(times / 29030400)), "years,", int(times / 2419200 % 12), "months,", int(times / 604800 % 4), "weeks,", int(times / 86400 % 7), "days,", int(times / 3600 % 24), "hours,", int(times / 60 % 60), "minutes and", int(times % 60), "seconds")
                            else:
                                print("The file", os.path.abspath(sourcefile), "was successfully encrypted as", os.path.abspath(destfile), "in\n" + str(int(times / 2419200)), "months,", int(times / 604800 % 4), "weeks,", int(times / 86400 % 7), "days,", int(times / 3600 % 24), "hours,", int(times / 60 % 60), "minutes and", int(times % 60), "seconds")
                        else:
                            print("The file", os.path.abspath(sourcefile), "was successfully encrypted as", os.path.abspath(destfile), "in\n" + str(int(times / 604800)), "weeks,", int(times / 86400 % 7), "days", int(times / 3600 % 24), "hours,", int(times / 60 % 60), "minutes and", int(times % 60), "seconds")
                    else:
                        print("The file", os.path.abspath(sourcefile), "was successfully encrypted as", os.path.abspath(destfile), "in\n" + str(int(times/ 86400)), "days,", int(times / 3600 % 24), "hours,", int(times / 60 % 60), "minutes and", int(times % 60), "seconds")
                else:
                    print("The file", os.path.abspath(sourcefile), "was successfully encrypted as", os.path.abspath(destfile), "in\n" + str(int(times / 3600)), "hours,", int(times / 60 % 60), "minutes and", int(times % 60), "seconds" )
            else:
                print("The file", os.path.abspath(sourcefile), "was successfully encrypted as", os.path.abspath(destfile), "in\n" + str(int(times / 60)), "minutes and",  int(times % 60), "seconds")
        else:
            print("The file", os.path.abspath(sourcefile), "was successfully encrypted as", os.path.abspath(destfile), "in", times, "seconds")

    time.sleep(2)

def myDecoding(sourcefile, destfile, password, read):
    byteCounter = 1
    filesize = os.path.getsize(sourcefile)
    average = round(filesize / 29127.11111)

    if average == 0:
        print("Propably time until finnish: less than 1 second")
    else:
        if average > 60:
            if average / 60 >= 60:
                if average / 3600 >= 24:
                    if average / 86400 >= 7:
                        if average / 604800 >= 4:
                            if average / 2419200 >= 12:
                                if average / 29030400 >= 100:
                                    print("Propably time until finish:", int(average / 2903040000), "centuries,", int(average / 29030400 % 100), "years", int(average / 2419200 % 12), "months,", int(average / 604800 % 4), "weeks,", int(average / 86400 % 7), "days,", int(average / 3600 % 24), "hours,", int(average / 60 % 60), "minutes and", int(average % 60), "seconds")
                                else:
                                    print("Propably time until finish:", int(average / 29030400), "years,", int(average / 2419200 % 12), "months,", int(average / 604800 % 4), "weeks,", int(average / 86400 % 7), "days,", int(average / 3600 % 24), "hours,", int(average / 60 % 60), "minutes and", int(average % 60), "seconds")
                            else:
                                print("Propably time until finish:", int(average / 2419200), "months,", int(average / 604800 % 4), "weeks,", int(average / 86400 % 7), "days,", int(average / 3600 % 24), "hours,", int(average / 60 % 60), "minutes and", int(average % 60), "seconds")
                        else:
                            print("Propably time until finish:", int(average / 604800), "weeks,", int(average / 86400 % 7), "days", int(average / 3600 % 24), "hours,", int(average / 60 % 60), "minutes and", int(average % 60), "seconds")
                    else:
                        print("Propably time until finish:", int(average/ 86400), "days,", int(average / 3600 % 24), "hours,", int(average / 60 % 60), "minutes and", int(average % 60), "seconds")
                else:
                    print("Propably time until finish:", int(average / 3600), "hours,", int(average / 60 % 60), "minutes and", int(average % 60), "seconds" )
            else:
                print("Propably time until finish:", int(average / 60), "minutes and",  int(average % 60), "seconds")
        else:
            print("Propably time until finish:", average, "seconds")

    time.sleep(2)
    times = time.clock()

    if average <= 30:
        percentlist = [x for x in range(100) if not x % 20 == 0] + [100]
    else:
        percentlist = [100]

    count = 0

    with open(sourcefile, "rb") as source:
            with open(destfile, "wb") as dest:
                source.read(read)
                checkSum = abs(zlib.crc32(bytes(password, "utf8")))
                checkSum = bin(checkSum)[2:]

                while len(checkSum) < 32:
                    checkSum = "0" + checkSum

                Z3 = checkSum[0:8]
                Z2 = checkSum[8:16]
                Z1 = checkSum[16:24]
                Z0 = checkSum[24:32]
                random.seed(int((Z2 + Z1 + Z0), 2)) 
                readByte = source.read(1) 

                while readByte != b"":
                    dest.write(bytes([(int.from_bytes(readByte, "big") - int(Z3, 2) - random.randint(0, 255) - int.from_bytes(bytes(password[count], "utf8"), "big")) % 256]))  

                    if count <= len(password) - 2:
                        count += 1
                    else: 
                        count = 0

                    percentage = math.floor(byteCounter / filesize * 100)

                    if percentage not in percentlist:
                        print("%0.2d" %int(percentage), "% finnished")
                        percentlist.append(int(percentage))

                    byteCounter += 1
                    readByte = source.read(1)
    times = round(time.clock() - times)

    if times == 0:
        print("The file", os.path.abspath(sourcefile), "was successfully encrypted as", os.path.abspath(destfile), "in less than 1 second")
    else:
        if times > 60:
            if times / 60 >= 60:
                if times / 3600 >= 24:
                    if times / 86400 >= 7:
                        if times / 604800 >= 4:
                            if times / 2419200 >= 12:
                                if times / 29030400 >= 100:
                                    print("The file", os.path.abspath(sourcefile), "was successfully decrypted as", os.path.abspath(destfile), "in\n" + str(int(times / 2903040000)), "centuries,", int(times / 29030400 % 100), "years", int(times / 2419200 % 12), "months,", int(times / 604800 % 4), "weeks,", int(times / 86400 % 7), "days,", int(times / 3600 % 24), "hours,", int(times / 60 % 60), "minutes and", int(times % 60), "seconds")
                                else:
                                    print("The file", os.path.abspath(sourcefile), "was successfully decrypted as", os.path.abspath(destfile), "in\n" + str(int(times / 29030400)), "years,", int(times / 2419200 % 12), "months,", int(times / 604800 % 4), "weeks,", int(times / 86400 % 7), "days,", int(times / 3600 % 24), "hours,", int(times / 60 % 60), "minutes and", int(times % 60), "seconds")
                            else:
                                print("The file", os.path.abspath(sourcefile), "was successfully decrypted as", os.path.abspath(destfile), "in\n" + str(int(times / 2419200)), "months,", int(times / 604800 % 4), "weeks,", int(times / 86400 % 7), "days,", int(times / 3600 % 24), "hours,", int(times / 60 % 60), "minutes and", int(times % 60), "seconds")
                        else:
                            print("The file", os.path.abspath(sourcefile), "was successfully decrypted as", os.path.abspath(destfile), "in\n" + str(int(times / 604800)), "weeks,", int(times / 86400 % 7), "days", int(times / 3600 % 24), "hours,", int(times / 60 % 60), "minutes and", int(times % 60), "seconds")
                    else:
                        print("The file", os.path.abspath(sourcefile), "was successfully decrypted as", os.path.abspath(destfile), "in\n" + str(int(times/ 86400)), "days,", int(times / 3600 % 24), "hours,", int(times / 60 % 60), "minutes and", int(times % 60), "seconds")
                else:
                    print("The file", os.path.abspath(sourcefile), "was successfully decrypted as", os.path.abspath(destfile), "in\n" + str(int(times / 3600)), "hours,", int(times / 60 % 60), "minutes and", int(times % 60), "seconds" )
            else:
                print("The file", os.path.abspath(sourcefile), "was successfully decrypted as", os.path.abspath(destfile), "in\n" + str(int(times / 60)), "minutes and",  int(times % 60), "seconds")
        else:
            print("The file", os.path.abspath(sourcefile), "was successfully decrypted as", os.path.abspath(destfile), "in", times, "seconds")
    time.sleep(2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cipher", action = "store_true", dest = "c", help = "use this argument to encrypt a file")
    parser.add_argument("-d", "--decipher", action = "store_true", dest = "d", help = "use this argument to decrypt a file")
    parser.add_argument("-p", "--password", type = str, dest = "password", help = "this is a reqiured argument. Type your password here")
    parser.add_argument("-i", "--inputfile", type = str, dest = "sourcefile", help = "this is a required argument. Type your inputfile here")
    parser.add_argument("-o", "--outputfile", type = str, default = "default", dest = "destfile", help = "use that optional argument to set your outputfile. The file is always: [your input].cip")
    args = parser.parse_args()

    if args.c == False and args.d == False:
        while True:
            cd = input("Do you want to Cipher (-c) or decipher (-d)? ")

            if cd == "-c":
                args.c = True
                break
            elif cd == "-d":
                args.d = True
                break
            else:
                print("Invalid input")

    if args.password is None:
        while True:
            args.password = getpass.getpass()

            if args.password == "":
                print("None type isn't allowed")
            else:
                break

    if args.sourcefile is None:
        while True:
            s = input("Type your sourcefilepath here: ")

            if s is None:
                print("Invalid input")
            else:
                args.sourcefile = s
                break

    if args.destfile == "default":
        while True:
            d = input("Do you really want to let the destfile generate automaticly? (Y/new Name)")

            if d == "Y" or d == "y" or d == "Yes" or d == "yes":
                break
            elif d is None:
                print("No input")
            else:
                args.destfile = d
                break

    with open(args.sourcefile, "rb") as s:
        s.read(3)
        toRead = 0

        try:
            toRead = 4 + int(s.read(1))
        except ValueError:
            d = 1

    with open(args.sourcefile, "rb") as s:
        if args.destfile == "default" and args.c == True:
            args.destfile = args.sourcefile.rsplit(".", 1)[0] + ".cip"
        elif args.destfile == "default" and args.d == True:
            args.destfile = args.sourcefile.rsplit(".", 1)[0]

        if args.d:
            if not s.read(3) == b"cip":
                raise FileNotSupportedError("That file isn't supported")

            if len(args.destfile.rsplit(".", 1)) == 1:
                ending = s.read(int(s.read(1)))
                args.destfile += "." + ending.decode("utf8")

        if not os.path.isfile(args.sourcefile):
            raise FileNotFoundError("Sourcefile does not Exist in that directory")

        if os.path.isfile(args.destfile):
            while True:
                g = input("destfile does already exist in that directory. Do you want to replace it?(Y/N)")

                if g == "Y" or g == "y":
                    break
                elif g == "N" or g == "n":
                    raise FileExistsError("destfile does already exist in that directory. Please change the directory")
                else:
                    raise InputError("Invalid input")

        if args.c == True and args.d == False:
            myEncoding(args.sourcefile, args.destfile, args.password)

        elif args.d == True and args.c == False:
            myDecoding(args.sourcefile, args.destfile, args.password, toRead)

        elif args.c == False and args.d == False:
            raise TypeError("One of the following arguments are required: -c/--cipher, -d/--decipher")

        elif args.c == True and args.d == True:
            raise TypeError("Only one of the following arguments is allowed: -c/--cipher, -d/--decipher")