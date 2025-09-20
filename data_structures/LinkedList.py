class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,newNode):
        if self.head is None:
            self.head=newNode
            return
        if self.head.data>=newNode.data:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
            return
        
        curr=self.head
    
        while curr.next and curr.next.data < newNode.data:
            if curr.next.data>newNode.data:
               break
            curr=curr.next
        newNode.next=curr.next
        curr.next=newNode
        newNode.prev=curr
    def delete(self,deleteNode):
        curr=self.head
        if self.head and self.head.data==deleteNode:
            self.head=curr.next
            if self.head:
                self.head.prev = None
            return

        while curr:
            if curr.data==deleteNode:
                curr.prev.next=curr.next
                if curr.next:              
                    curr.next.prev = curr.prev
                return  
            curr=curr.next


    def display():
        LL=LinkedList()
        while True:
            choose_LL=int(input("choose Linked List method:\n" \
            "1.insert\n" 
            "2.delete \n"
            "3.exit\n"))
            if choose_LL==1:
                LL.insert(Node(int(input("enter value to insert: "))))
            elif choose_LL==2:
                LL.delete(int(input("enter a value to  delete: ")))
            else:
                break
            curr=LL.head
            while curr:
                print(curr.data,end='<->')
                curr=curr.next
            print("None")
            

                

 




















