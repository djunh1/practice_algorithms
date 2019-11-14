def heapify(arr, arrLen, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
 
    if l < arrLen and arr[i] < arr[l]:
        largest = l
 
    if r < arrLen and arr[largest] < arr[r]:
        largest = r
 
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, arrLen, largest)
 
def heapSort(arr):
    arrLen = len(arr)
 
    # Build max heap
    for i in range(arrLen, 0, -1):
        heapify(arr, arrLen, i)
 
    
    for i in range(arrLen-1, 0, -1):
        # swap
        arr[i], arr[0] = arr[0], arr[i]  
        
        
arr = [ 12,3, 11, 13, 5, 6, 7,2]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i])