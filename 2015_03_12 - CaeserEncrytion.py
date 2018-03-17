def encodeWithCaesar(sourcefile, destfile, caesarPass):
    count = 0
    counter = 0
    print("encryption running\n")
    with open(sourcefile, "rb") as source:
        with open(destfile, "wb") as dest:
            readByte = source.read(1)
            while readByte != b"":
                dezNumber = int.from_bytes(readByte, "big")
                dezPass = int.from_bytes(bytes(caesarPass[count], "utf8"), "big")
                dezdest = dezNumber + dezPass
                dezdest %= 255
                dest.write(bytes([dezdest]))
                counter += 1
                if count <= len(caesarPass) - 2:
                    count += 1
                else:
                    count = 0
                readByte = source.read(1)
    print("encryption finished\n\n")


def decodeWithCaesar(sourcefile, destfile, caesarPass):
    count = 0
    print("decryption running\n")
    with open(sourcefile, "rb") as source:
        with open(destfile, "wb") as dest:
            readByte = source.read(1)
            while readByte != b"":
                dezNumber = int.from_bytes(readByte, "big")
                dezPass = int.from_bytes(bytes(caesarPass[count], "utf8"), "big")
                dezdest = dezNumber - dezPass
                dezdest %= 255
                dest.write(bytes([dezdest]))
                if count <= len(caesarPass) - 2:
                    count += 1
                else:
                    count = 0
                readByte = source.read(1)
    print("decryption finished\n")