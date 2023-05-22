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
        
    def printListInReverse(self):
        currentNode = self.nextNode
        arr = []
        print("")
        while currentNode is not None:
            arr.append(currentNode.data)
            currentNode = currentNode.nextNode
        i = len(arr)
        while i > 0:
            print(arr[i-1])
            i -= 1
    
    def insertAtEnd(self,data):
        currentNode = self.nextNode
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode
        currentNode.nextNode = Node(data)
    
    def insertAtStart(self,data):
        oldNextNode = self.nextNode
        self.nextNode = Node(data)
        self.nextNode.nextNode = oldNextNode
    
    def delFromEnd(self):
        currentNode = self.nextNode
        while currentNode.nextNode.nextNode is not None:
            currentNode = currentNode.nextNode
        currentNode.nextNode = None
    
    def delFirstNode(self):
        if self.nextNode is None:
            print("List is empty")
            return
        self.nextNode = self.nextNode.nextNode

    def delNode(self, dataToDel):
        if self.nextNode is None:
            print("cannot delete because List is empty")
            return
        if self.nextNode.data == dataToDel:
            self.delFirstNode()
        currentNode = self.nextNode
        previousNode = None
        while currentNode is not None:
            if currentNode.data == dataToDel: #cheaks to nodes in advance/hard to change previous node
                if currentNode.nextNode is None:
                    previousNode.nextNode = None
                    return
                else:
                    previousNode.nextNode = currentNode.nextNode
                    return
            else:
                previousNode = currentNode
                currentNode = currentNode.nextNode
        print(dataToDel,"was not in the list")
    
        

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
list1.delFromEnd() #removed from end
list1.printList()
print()
list1.delFromStart() #removed from start
list1.printList()