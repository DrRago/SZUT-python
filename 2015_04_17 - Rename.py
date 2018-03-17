import os
delete = " (1080p 60fps)"
path = "D:\\Neu und so\\LoL\\"
files = os.listdir(path)
for fname in files:
    newname = "".join(map(str, fname.split(delete)))
    os.rename(path + fname, path + newname)