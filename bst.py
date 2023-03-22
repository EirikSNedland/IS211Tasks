class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.data:
            if self.data > data:
               if self.left == None:
                   self.left = Node(data)
               else:
                   self.left.insert(data)
            else:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        print(self.data, " :")
        if self.left:
            print( " left branch: ", self.left.data)  
        else:
            print( " has no left branch")
        if self.right:
            print( " right branch: ", self.right.data)
        else:
            print( " has no right branch")
        if self.left:
            self.left.printTree()
        if self.right:    
            self.right.printTree()
        

tree = Node(21)

tree.insert(28)
tree.insert(14)
tree.insert(18)
tree.insert(11)
tree.insert(15)
tree.insert(19)
tree.insert(32)
tree.insert(30)
tree.insert(25)

tree.printTree()
