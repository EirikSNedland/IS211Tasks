#Merge sort algorithm, Time complexity: O(N log(N))
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 #Divide array into left and right
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L) #further divide each of the half into left and right
        mergeSort(R) #Time complexity is O(log n) 
        
        i=j=k=0
        
        while i < len(L) and j < len(R): #assemble the halfs into array
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j+=1
            k +=1
        
        #dette er en check for å forsikre om at ingenting var glemt
        # var nædvendig ellers ble slutt resultatet feil
        # sette array sammen igjen sortert O(n)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    #timecomplexity O(n log n)

def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

arr=[1,64,7,3,8,9,124,24,25,2]

mergeSort(arr)

printList(arr)