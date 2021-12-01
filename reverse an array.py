l = list(map(int, input('enter array: ').split()))
for x in range(int(len(l) / 2)):
    a = l[len(l) - 1 - x]
    l[len(l) - x - 1] = l[x]
    l[x] = a
print(l)
