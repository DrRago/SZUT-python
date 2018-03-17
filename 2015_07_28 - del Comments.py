__author__ = 'Leonhard Gahr'

import os
filename = str(input("Filename (this file has to be in the same directiory!!!): "))
var = 0
with open(filename, "r") as source:
    with open("new.temp", "w") as dest:
        for i in source:
            var = 0
            for x in i:
                if var == 1:
                    continue
                if x != "#":
                    dest.write(x)
                else:
                    var = 1
                    dest.write("\n")

os.remove(filename)
os.rename("new.temp", filename)