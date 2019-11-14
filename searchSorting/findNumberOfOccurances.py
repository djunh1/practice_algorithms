
def pr_N_mostFrequentNumber(arr, arrLength, freq): 

    um = {} 
    for i in range(arrLength): 
        if arr[i] in um: 
            um[arr[i]] += 1
        else: 
            um[arr[i]] = 1
    a = [0] * (len(um)) 
    j = 0
    for i in um: 
        a[j] = [i, um[i]] 
        j += 1
    a = sorted(a, key = lambda x : x[0], reverse = True) 
    a = sorted(a, key = lambda x : x[1], reverse = True) 
                        

    print(freq, "numbers with most occurrences are:") 
    for i in range(freq): 
        print(a[i][0], end = " ") 


if __name__ =="__main__": 
    arr = [3, 1, 4, 4, 5, 2, 6, 1] 
    arrLength = 8
    freq = 2
    pr_N_mostFrequentNumber(arr, arrLength, freq) 

