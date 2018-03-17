def divisor(i):
    f = 1
    total = 0
    while f <= i / 2:
        if i % f == 0:
            total += f
        f += 1
    return total

z = int(input("Bitte die Grenze eingeben: "))
sums = {}
for i in range(1, z + 1):
    sums[i] = divisor(i)
numbers = 0
count = 0
for a in range(1, z + 1):
    for b in range(1, a):
        if a != b and sums[a] == b and sums[b] == a:
            print(a, 'und', b, 'sind befreundet')
            numbers += 2
        if a % b == 0:
            count += b
    if count == a:
        if a != 0:
            print(a, "ist vollkommen")
            numbers += 1
    count = 0
if numbers == 1:
    print("Es wurde eine Zahl ausgegeben")
else:
    print("Es wurden", numbers, "Zahlen ausgegeben")