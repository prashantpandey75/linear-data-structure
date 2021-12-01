class stack():
    def __init__(self):
        self.main_stack = []
        self.help_stack = []

    def push(self, item):
        self.main_stack.append(item)
        if len(self.help_stack) >= 1:
            if self.help_stack[-1] >= item:
                self.help_stack.append(item)
        else:
            self.help_stack.append(item)

    def pop(self):
        if len(self.main_stack) >= 1:
            popped_value = self.main_stack.pop()
            if popped_value == self.help_stack[-1]:
                self.help_stack.pop()

    def min_value(self):
        if len(self.help_stack) >= 1:
            return self.help_stack[-1]
        else:
            return None
obj = stack()
obj.push(2)
obj.push(3)
obj.push(2)
obj.push(5)
obj.push(6)
print(obj.min_value())
