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
