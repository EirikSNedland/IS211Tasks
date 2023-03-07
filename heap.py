import math
class Heap: ##work in progress, lacks insert, delete and more
    def __init__(self):
        self.list = []
    
    def swap(self, pos1, pos2):
        self.list[pos1], self.list[pos2] = self.list[pos2], self.list[pos1]

    def findLeaftChild(self,pos):
        return 2*pos+1
    
    def findRightChild(self,pos):
        return 2*pos+2
    
    def isLeafNode(self, pos):
        return pos * 2 > len(self.list)

    def heapify(self,pos):
        if not self.isLeafNode(pos):
            if self.findRightChild(pos) > len(self.list):
                print(self.findRightChild(pos), "right node at this index dont exist")
                return
            if self.findLeaftChild(pos) > len(self.list):
                print(self.findLeaftChild(pos), "left node at this index dont exist")
                return
            if (self.list[pos] > self.list[self.findLeaftChild(pos)] or 
                self.list[pos] > self.list[self.findRightChild(pos)]):
                if self.list[pos] > self.list[self.findLeaftChild(pos)]:
                    self.swap(pos,self.findLeaftChild(pos)) 
                    self.heapify(self.findLeaftChild(pos))
                else:
                    self.swap(pos,self.findRightChild(pos)) 
                    self.heapify(self.findRightChild(pos))

    def heapSort(self):
        i = math.floor(len(self.list)//2)
        for pos in range(i, -1,-1):
            self.heapify(pos)
            
    def printList(self):
        for i in range(1, len(self.list)//2):
            print(" PARENT : "+ str(self.list[i])+" LEFT CHILD : "+ 
                                str(self.list[2 * i + 1])+" RIGHT CHILD : "+
                                str(self.list[2 * i + 2]))
   
heap = Heap()
heap.list = [19,13,15,3,7,4,8,9,10,11,16,12,1,5,6,21,32,20,24]
heap.heapSort()
print(heap.list)
heap.heapSort() ##need to run sort twice to get it heap sorted
print(heap.list)
heap.heapSort()
print(heap.list)
heap.printList()
