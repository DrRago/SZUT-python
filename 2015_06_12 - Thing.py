__author__ = 'Drrago'

import sys

class Thing(object):

    __concentration = {"Fe": 7.87,
                    "Au": 19.32,
                    "Ag": 10.5}

    __element = {"Fe": "Iron",
                 "Au": "Gold",
                 "Ag": "Silver"}

    def __init__(self, volume, symbol):
        self.__volume = volume
        self.__symbol = symbol

    def getMass(self):
        return self.__volume * self.__concentration[self.__symbol]

    def getVolume(self):
        return self.__volume

    def __str__(self):
        return str(round(self.getMass(), 3)) + " cubic centimeters " + str(self.__element[self.__symbol])

    def __gt__(self, *args):
        return self.getMass() > args[0].getMass()

    def __ge__(self, *args):
        return self.getMass() >= args[0].getMass()

    def __lt__(self, *args):
        return self.getMass() < args[0].getMass()

    def __le__(self, *args):
        return self.getMass() <= args[0].getMass()

    def __eq__(self, *args):
        return self.getMass() == args[0].getMass()

class Cuboid(Thing):

    __concentration = {"Fe": 7.87,
                    "Au": 19.32,
                    "Ag": 10.5}

    __element = {"Fe": "Iron",
                 "Au": "Gold",
                 "Ag": "Silver"}

    def __init__(self, lenght, width, height, symbol):
        Thing.__init__(self, lenght * width * height, symbol)
        self.__lenght = lenght
        self.__width = width
        self.__height = height
        self.__symbol = symbol
        self.__volume = self.__lenght * self.__width * self.__height

    def __str__(self):
        return str(round(self.getMass(), 3)) + " cubic centimeters " + str(self.__element[self.__symbol]) + " --- Cuboid: " + str(self.__lenght) + " * " + str(self.__width) + " * " + str(self.__height)

    def __gt__(self, *args):
        return self.getMass() > args[0].getMass()

    def __ge__(self, *args):
        return self.getMass() >= args[0].getMass()

    def __lt__(self, *args):
        return self.getMass() < args[0].getMass()

    def __le__(self, *args):
        return self.getMass() <= args[0].getMass()

    def __eq__(self, *args):
        return self.getMass() == args[0].getMass()


if __name__ == "__main__":
    lenght1 = 0
    lenght2 = 0
    width1 = 0
    width2 = 0
    height1 = 0
    height2 = 0
    symbol1 = ""
    metalList = {"Fe": "Iron",
                 "Au": "Gold",
                 "Ag": "Silver",
                 "Li": "Lithium",
                 "Na": "Sodium",
                 "K": "Potassium",
                 "Rb": "Rubidium",
                 "CS": "Caesium",
                 "Fr": "Francium",
                 "Be": "Beryllium",
                 "Mg": "Magnesium",
                 "Ca": "Calcium",
                 "Sr": "Strontium",
                 "Ba": "Barium",
                 "Ra": "Radium",
                 "Sc": "scandium",
                 "Y": "Yttrium",}


    symbol1 = input("Please insert the elementsymbol or the ordinal of your metal: ")
    while symbol1 not in metalList:
        symbol1 = input("That element isn't supported, try again: ")
    volume1 = input('Please insert the volume of your %s ingot (If unknow, insert "none"): ' % metalList[symbol1])
    while True:
        if volume1 == "none":
            try:
                lenght1 = float(input("Please insert the lenght of your %s ingot: " % metalList[symbol1]))
                width1 = float(input("Please insert the width of your %s ingot: " % metalList[symbol1]))
                height1 = float(input("Please insert the height of your %s ingot: " % metalList[symbol1]))
                break
            except ValueError:
                print("Oops, couldn't convert your volume to a float! Try again")
                lenght1 = ""
                width1 = ""
                height1 = ""
            except:
                print("Unexpected error:", sys.exc_info()[0])
                lenght1 = ""
                width1 = ""
                height1 = ""
                raise
        elif volume1 == "":
            volume1 = str(input('Please insert the volume of your %s ingot (If unknow, insert "none"): ' % metalList[symbol1]))
        else:
            try:
                volume1 = float(volume1)
                break
            except ValueError:
                print("Oops, couldn't convert your volume to a float! Try again")
                volume1 = ""
            except:
                print("Unexpected error:", sys.exc_info()[0])
                volume1 = ""
                raise

    operation = input('Do you want to compare two ingots, insert nothing, or insert "no" to leave it at one: ')
    if operation == "":

        symbol2 = input("Please insert the elementsymbol of your second metal: ")
        while symbol2 not in metalList:
            symbol2 = str(input("That element isn't supported, try again: "))

        volume2 = input('Please insert the volume of your %s ingot (If unknow, insert "none"): ' % metalList[symbol2])
        while True:
            if volume2 == "none":
                try:
                    lenght2 = float(input("Please insert the lenght of your %s ingot: " % metalList[symbol2]))
                    width2 = float(input("Please insert the width of your %s ingot: " % metalList[symbol2]))
                    height2 = float(input("Please insert the height of your %s ingot: " % metalList[symbol2]))
                    break
                except ValueError:
                    print("Oops, couldn't convert your volume to a float! Try again")
                    lenght2 = ""
                    width2 = ""
                    height2 = ""
                except:
                    print("Unexpected error:", sys.exc_info()[0])
                    lenght2 = ""
                    width2 = ""
                    height2 = ""
                    raise
            elif volume2 == "":
                volume2 = input('Please insert the volume of your %s ingot (If unknow, insert "none"): ' % metalList[symbol2])
            else:
                try:
                    volume2 = float(volume2)
                    break
                except ValueError:
                    print("Oops, couldn't convert your volume to a float! Try again")
                    volume2 = ""
                except:
                    print("Unexpected error:", sys.exc_info()[0])
                    volume2 = ""
                    raise
        try:
            if volume1 == "none" and volume2 == "none":
                if Cuboid(lenght1, width1, height1, symbol1) > Cuboid(lenght2, width2, height2, symbol2):
                    print("Ingot", Cuboid(lenght1, width1, height1, symbol1), "is bigger than Ingot", Cuboid(lenght2, width2, height2, symbol2))

                if Cuboid(lenght1, width1, height1, symbol1) < Cuboid(lenght2, width2, height2, symbol2):
                    print("Ingot", Cuboid(lenght1, width1, height1, symbol1), "is less than Ingot", Cuboid(lenght2, width2, height2, symbol2))

                if Cuboid(lenght1, width1, height1, symbol1) == Cuboid(lenght2, width2, height2, symbol2):
                    print("Ingot", Cuboid(lenght1, width1, height1, symbol1), "is equal to Ingot", Cuboid(lenght2, width2, height2, symbol2))

            if volume1 != "none" and volume2 != "none":
                if Thing(volume1, symbol1) > Thing(volume2, symbol2):
                    print("Ingot", Thing(volume1, symbol1), "is bigger than Ingot", Thing(volume2, symbol2))

                if Thing(volume1, symbol1) < Thing(volume2, symbol2):
                    print("Ingot", Thing(volume1, symbol1), "is less than Ingot", Thing(volume2, symbol2))

                if Thing(volume1, symbol1) == Thing(volume2, symbol2):
                    print("Ingot", Thing(volume1, symbol1), "is equal to Ingot", Thing(volume2, symbol2))

            if volume1 != "none" and volume2 == "none":
                if Thing(volume1, symbol1) > Cuboid(lenght2, width2, height2, symbol2):
                    print("Ingot", Thing(volume1, symbol1), "is bigger than", Cuboid(lenght2, width2, height2, symbol2))

                if Thing(volume1, symbol1) < Cuboid(lenght2, width2, height2, symbol2):
                    print("Ingot", Thing(volume1, symbol1), "is less than", Cuboid(lenght2, width2, height2, symbol2))

                if Thing(volume1, symbol1) == Cuboid(lenght2, width2, height2, symbol2):
                    print("Ingot", Thing(volume1, symbol1), "is equal to", Cuboid(lenght2, width2, height2, symbol2))

            if volume1 == "none" and volume2 != "none":
                if Cuboid(lenght1, width1, height1, symbol1) > Cuboid(lenght2, width2, height2, symbol2):
                    print("Ingot", Thing(volume1, symbol1), "is bigger than", Thing(volume2, symbol2))

                if Cuboid(lenght1, width1, height1, symbol1) < Cuboid(lenght2, width2, height2, symbol2):
                    print("Ingot", Thing(volume1, symbol1), "is less than", Thing(volume2, symbol2))

                if Cuboid(lenght1, width1, height1, symbol1) == Cuboid(lenght2, width2, height2, symbol2):
                    print("Ingot", Thing(volume1, symbol1), "is equal to", Thing(volume2, symbol2))
        except:
            print("Whoops, something unexpected is wrong", sys.exc_info()[0])
            raise

    elif operation == "no":
        if volume1 == "none":
            print(Cuboid(lenght1, width1, height1, symbol1))
        elif volume1 != "none":
            print(Thing(volume1, symbol1))