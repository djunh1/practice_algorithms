
def mergeSort(arr): 
    if len(arr) >1: 
        middle = len(arr)//2 #Finding the middle of the array 
        Left = arr[:middle] # Dividing the array elements 
        Right = arr[middle:] # into 2 halves 

        mergeSort(Left) # Sorting the first half 
        mergeSort(Right) # Sorting the second half 

        i = j = k = 0
        
        while i < len(Left) and j < len(Right): 
            if Left[i] < Right[j]: 
                arr[k] = Left[i] 
                i+=1
            else: 
                arr[k] = Right[j] 
                j+=1
            k+=1
        
        # Checking if any element was left 
        while i < len(Left): 
            arr[k] = Left[i] 
            i+=1
            k+=1
        
        while j < len(Right): 
            arr[k] = Right[j] 
            j+=1
            k+=1


def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 


if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7] 
    print ("Given array is", end="\n") 
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 


