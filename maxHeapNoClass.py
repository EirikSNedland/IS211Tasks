def maxHeapSort(arr):
    n = len(arr)
    for i in range((n//2)-1,-1,-1):
        maxHeapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        maxHeapify(arr,i,0)

def maxHeapify(arr,n,i):
    biggest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[biggest] < arr[l]:
        biggest = l
    
    if r < n and arr[biggest] < arr[r]:
        biggest = r
    
    if biggest != i:
        arr[biggest],arr[i] = arr[i], arr[biggest]
        maxHeapify(arr,n,biggest)

arr3 = [2,8,5,3,9]

maxHeapSort(arr3)