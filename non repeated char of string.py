l =input('enter array: ')
d={i:0 for i in l}
#print(d)
for i in l:
    if i in d:
        d[i]=d[i]+1


for i in d:
    if d[i]==1:
        print(i)
        break