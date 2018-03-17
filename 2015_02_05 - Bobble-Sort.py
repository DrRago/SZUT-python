from random import randint
k = 0
c = 0
rounds = 0
compares = 0
switches = 0
list = []
for i in range(20):
    list.append(randint(1, 10000))
print(' '.join(map(str, list)))
n = len(list)
while n > 1:
    rounds += 1
    newn = 1
    for i in range(n-1):
        compares += 1
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            newn = i + 1
            switches += 1
        n = newn
print(', '.join(map(str, list)))
print("Durchläufe:", rounds)
print("Vergleiche:", compares)
print("Täusche:", switches)