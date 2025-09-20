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
        
    def display():
        st = stack([])
        while True:
            choose_stack = int(input("Choose stack method:\n"
                                    "1. Push \n"
                                    "2. Pop \n"
                                    "3. Peek \n"
                                    "4. Size\n"
                                    "5.exit\n"))
            if choose_stack == 1:
                st.push(int(input("Enter number to push: ")))
            elif choose_stack == 2:
                st.pop()
            elif choose_stack == 3:
                st.peek()
            elif choose_stack == 4:
                st.size()
            elif choose_stack==5:
                break