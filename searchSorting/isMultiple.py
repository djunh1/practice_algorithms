
def isMultipleOf3(n): 

    odd_count = 0
    even_count = 0

    if(n < 0): 
        n = -n 
    if(n == 0): 
        return 1
    if(n == 1): 
        return 0

    while(n): 
        if(n & 1): 
            odd_count += 1

        if(n & 2): 
            even_count += 1
        n = n >> 2

    return isMultipleOf3(abs(odd_count - even_count)) 


num = 24
if (isMultipleOf3(num)): 
    print(num, 'is multiple of 3') 
else: 
    print(num, 'is not a multiple of 3') 

# This code is contributed by Danish Raza 
