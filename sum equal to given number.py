a = list(map(int, input('enter array').split()))
sum = int(input('enter sum required: '))
for x in range(len(a) - 1):
    for y in range(x + 1, len(a)):
        if a[x] + a[y] == sum:
            print('pair is', a[x], a[y])
        else:
            pass
