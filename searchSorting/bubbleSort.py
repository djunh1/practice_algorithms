
def bubbleSort(arr): 
    arrLen = len(arr) 
    
    for idx in range(arrLen): 
        swapped = False
        arrLenLeft = arrLen-idx-1
        
        for j in range(0, arrLenLeft): 
            
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True

        if swapped == False: 
            break
        
arr = [64, 34, 25, 12, 22, 11, 90] 

bubbleSort(arr) 

print ("Sorted array :") 
for i in range(len(arr)): 
    print ("%d" %arr[i],end=" ") 

