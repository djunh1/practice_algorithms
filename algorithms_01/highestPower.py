 
def highestPowerof2(n): 

    res = 0; 
    for i in range(n, 0, -1): 
        
        # If i is a power of 2 
        if ((i & (i - 1)) == 0): 
        
            res = i; 
            break; 
        
    return res; 


def isPowerOfTwo(n): 
    if (n == 0): 
        return False
    while (n != 1): 
            if (n % 2 != 0): 
                return False
            n = n // 2
              
    return True


n = 10; 
print(highestPowerof2(n)); 

if(isPowerOfTwo(31)): 
    print('Yes') 
else: 
    print('No') 
