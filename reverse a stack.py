class reverse():
    def __init__(self):
        self.a = []
        self.b = []

    def push(self, item):
        self.a.append(item)

    def pop(self):
        self.a.pop()

    def rev(self):
        for i in range(len(self.a)):
            popped_value = self.a.pop()
            #print(popped_value, i)
            self.b.append(popped_value)
        print(self.b)

obj = reverse()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.rev())