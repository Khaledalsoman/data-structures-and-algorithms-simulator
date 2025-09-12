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
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")









