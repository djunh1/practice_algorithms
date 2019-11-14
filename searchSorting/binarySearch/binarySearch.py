from builtins import int
from linearSearch.linearSearch import arr

def binarySearch(arr, low, arrLength, targetVar): 

    while low <= arrLength: 
        middle = int( low +  (arrLength - low)/2 );      
        if arr[middle] == targetVar: 
            return middle 
        elif arr[middle] < targetVar: 
            low = middle + 1
        else: 
            arrLength = middle - 1
    return -1

arr = [2,3,5,6,7,8,10] 
x = int(10)

result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
    print("Element is present at index", result); 
else: 
    print ("Element is not present in array")


if __name__ == '__main__':
    pass