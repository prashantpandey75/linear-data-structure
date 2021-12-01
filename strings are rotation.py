a=input("enter a string: ")
b=input('enter string to check: ')
c=a+b

if len(a)!=len(b):
    print('rotation not possible')
else:
    if a in c:
        print('rotation possible')
    else:
        print('no')