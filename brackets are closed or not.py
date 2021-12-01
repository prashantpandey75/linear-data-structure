class Stack:
    def __init__(self, size):
        self.size = size
        self.data = []
        self.length = 0
        self.top = None

    def push(self, item):
        if self.length < self.size:
            self.data.append(item)
            self.length += 1
            self.top = item
        else:
            print('stack is overflow')

    def pop(self):
        if self.length == 0:
            print('stack is under flow')
        else:
            self.data.pop()
            self.length -= 1
            if self.length == 0:
                self.top = None
            else:
                self.top = self.data[-1]

    def peek(self):
        return self.top


stack_obj = Stack(20)
expression = input('enter expression: ')
partner = {']': '[', ')': '(', '}': '{'}

for i in expression:
    if i in partner.values():
        stack_obj.push(i)
    else:
        if stack_obj.length == 0:
            print('NOT CLOSED')
            break
        else:
            if partner[i] == stack_obj.peek():
                stack_obj.pop()
            else:
                print('NOT CLOSED')
                break
else:
    if stack_obj.length != 0:
        print('NOT CLOSED')
    else:
        print('CLOSED')