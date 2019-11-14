
def search(pattern, txt): 
    
    patternLen = len(pattern) 
    txtlen = len(txt) 
    loopLength = txtlen - patternLen + 1

    for i in range(loopLength): 
        j = 0
        
        while(j < patternLen): 
            if (txt[i + j] != pattern[j]): 
                break
            j += 1

        if (j == patternLen): 
            print("Pattern found at index ", i) 

if __name__ == '__main__': 
    txt = "abcdABCDabcd"
    pattern = "ab"
    search(pattern, txt) 

