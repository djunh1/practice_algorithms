import sys 

Arr = [64, 25, 12, 22, 11] 
arrLength = len(Arr)
  

for i in range(arrLength): 
      
    min_idx = i 
    
    for j in range(i+1, arrLength): 
        if Arr[min_idx] > Arr[j]: 
            min_idx = j 
                      
    Arr[i], Arr[min_idx] = Arr[min_idx], Arr[i] 
  

print ("Sorted array") 
for i in range(len(Arr)): 
    print("%d" %Arr[i]),

if __name__ == '__main__':
    pass