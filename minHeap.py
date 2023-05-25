class MinHeap:
    def __init__(self,arr):
        self.arr = arr 

    #n list size
    #i = root
    def heapify(self,n,i):
        #It shall be a min heap (decending order requirment)
        smallest = i
        l = 2 * i + 1 #first element in list is 0, thats why + 1
        r = 2 * i + 2

        if l < n and self.arr[smallest] > self.arr[l]:
            smallest = l
        
        if r < n and self.arr[smallest] > self.arr[r]:
            smallest = r
        
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i] #swap
            self.heapify(n,smallest) #will cheack trhough the new smallest to se if childs are smaller than parent
        
    def heapSort(self):
        n = len(self.arr)
        #Time complexity of for loop is O(n) (is it tho, it only goes throug half so n/2)
        #time complexity of first heapify is O(log n)
        for i in range((n//2)-1,-1,-1): #- 1 after (n//2) because list start at 0 and not 1
            self.heapify(n,i)
        #time complexity of second for loop is O(n)
        for i in range(n-1,0,-1): #wanne go through the entire list again to compare against top, then heapify from top down
            self.arr[i],self.arr[0] = self.arr[0],self.arr[i]
            self.heapify(i,0) #time complexity O(log n) 
    #Time complexity of first loop: (n/2)*log n
    #Second loop is n * log n 
    #O((n/2)*logn)+ O(n*logn) fastest growing term is O(n*logn) 

arr = [9,4,7,3,8,2,1,89,23]

minHeapList = MinHeap(arr)
minHeapList.heapSort()
print(minHeapList.arr)
