class Stack():
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()


A = Stack()
n = str(input('....'))
for i in n:
    if i == '+' or i == '*' or i == '-' or i == '/':
        op1 = A.pop()
        op2 = A.pop()
        z = i + op2 + op1
        A.push(z)
    else:
        A.push(i)
print(A.stack[0])
