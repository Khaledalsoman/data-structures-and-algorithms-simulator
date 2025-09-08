class stack:
    def __init__(self,stack):
        self.stack=stack
    
    def push(self,item):
        self.stack.append(item)
        print(self.stack)

    def pop(self):
        if self.isEmpty():
            return None
        self.stack.pop()
        print(self.stack)

    def peek(self):
        if self.isEmpty():
            return None
        print(self.stack[-1])

    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        print(len(self.stack))