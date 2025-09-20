
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class trees:
    def preOrderTraversal(node):
        if node is None:
            return
        print(node.data, end=", ")
        trees.preOrderTraversal(node.left)
        trees.preOrderTraversal(node.right)
    def inOrderTraversal(node):
        if node is None:
            return
        trees.inOrderTraversal(node.left)
        print(node.data, end=", ")
        trees.inOrderTraversal(node.right)
    def postOrderTraversal(node):
        if node is None:
            return
        trees.postOrderTraversal(node.left)
        trees.postOrderTraversal(node.right)
        print(node.data, end=", ")
    def display():
        root = Node(input("Enter root: "))
        NodeA = Node(input("Enter left child of root: "))
        NodeB = Node(input("Enter right child of root: "))
        NodeC = Node(input("Enter left child of A: "))
        NodeD = Node(input("Enter right child of A: "))
        NodeE = Node(input("Enter left child of B: "))
        NodeF = Node(input("Enter right child of B: "))

        root.left=NodeA
        root.right=NodeB
        NodeA.left=NodeC
        NodeA.right=NodeD
        NodeB.left=NodeE
        NodeB.right=NodeF
        ChooseTreeTraversal=int(input("enter method you want to follow: \n" \
        "1.pre-order \n" \
        "2.in order \n" \
        "3.post order \n"))
        if ChooseTreeTraversal == 1:
            trees.preOrderTraversal(root)
        elif ChooseTreeTraversal == 2:
            trees.inOrderTraversal(root)
        elif ChooseTreeTraversal == 3:
            trees.postOrderTraversal(root)


