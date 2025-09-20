class queue:
    def __init__(self,queue):
        self.queue=queue


    def enqueue(self,item):
         self.queue.append(item)
         print(self.queue)
         return self.queue
    
    def dequeue(self):
        if self.isEmpty():
            return None
        self.queue.pop(0)
        print(self.queue)
    
    def peek(self):
        if self.isEmpty():
            return None
        print(self.queue[0])
        
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        print(len(self.queue))
    def display():
        qu=queue([])
        while True:
            choose_queue = int(input("choose queue method to use: \n" \
            "1.enqueue \n" \
            "2.dequeue \n" \
            "3.peek \n" \
            "4.size \n"
            "5.exit\n"))
            if choose_queue ==1:
                qu.enqueue(int(input('choose number to enqueue ')))
            elif choose_queue ==2:
                qu.dequeue()
            elif choose_queue ==3:
                qu.peek()
            elif choose_queue ==4:
                qu.size()
            elif choose_queue==5:
                break
