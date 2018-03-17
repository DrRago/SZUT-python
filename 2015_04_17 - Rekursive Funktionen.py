
def row(n):
    if n <= 1:
        return 1
    else:
        return 2*row(n-1)+1
print(row(100 + 1))

