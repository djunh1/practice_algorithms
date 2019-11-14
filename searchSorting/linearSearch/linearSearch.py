
def search(arr, arrLength, target): 

    for idx in range (0, arrLength): 
        if (arr[idx] == target): 
            return idx; 
    return -1; 


arr = [ 2, 3, 4, 10, 40 ]; 
target = 10; 
arrLength = len(arr); 
result = search(arr, arrLength, target) 


if(result == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", result); 


if __name__ == '__main__':
    pass