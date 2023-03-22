class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.nextNode = None
    
    def printList(self):
        currentNode = self.nextNode
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode
    
    def insertAtEnd(self,data):
        currentNode = self.nextNode
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode
        currentNode.nextNode = Node(data)
    
    def insertAtStart(self,data):
        oldNextNode = self.nextNode
        self.nextNode = Node(data)
        self.nextNode.nextNode = oldNextNode
    
    def removeFromEnd(self):
        currentNode = self.nextNode
        while currentNode.nextNode.nextNode is not None:
            currentNode = currentNode.nextNode
        currentNode.nextNode = None
    
    def removeFromStart(self):
        self.nextNode = self.nextNode.nextNode
    
        

list1 = LinkedList()

list1.nextNode = Node("first node")

list1.nextNode.nextNode = Node("SeCoNd NoDe")

list1.printList() #list at the moment
print()
list1.insertAtEnd("Third")
list1.insertAtEnd("Fourth")
list1.printList() #inserted at end
print()
list1.insertAtStart("Im first now")
list1.printList() #inserted at start
print()
list1.removeFromEnd() #removed from end
list1.printList()
print()
list1.removeFromStart() #removed from start
list1.printList()