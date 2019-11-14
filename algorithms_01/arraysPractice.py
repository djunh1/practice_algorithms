from _operator import index
import collections
import json 

def amagram(str1, str2):
    
    s1 = str1.replace(' ','').lower()
    s2 = str2.replace(' ', '').lower()
    
    if len(s1) != len(s2):
        return False
    
    
    countDict = {}
    
    for i in s1:
        if i in countDict:
            countDict[i] +=1
        else:
           countDict[i] = 1 
           
    for j in s2:
        if j in s2:
            countDict[j] -=1
        else:
            countDict[j] = 1
            
    for k in countDict:
        if countDict[k] != 0:
            return False
        
    return True
        
    
def array_pair(arr, num):
    
    seen = set()
    output = set()
    
    for i in arr:
        targetNumber = num - i
        
        if targetNumber not in seen:
            seen.add(i)
        else:
            output.add( (min(i,targetNumber) , max(i, targetNumber)) )
                       
                    
    print('\n'.join(map(str,list(output))))


def find_missing_number(arr1, arr2):
    
    arr1.sort()
    arr2.sort()
    
    for num1, num2 in zip(arr1,arr2):
        if num1!= num2:
            return num1
    
    
    return arr1[-1]

def find_missing_number2(arr1, arr2): 
    
    arrDict=collections.defaultdict(int) 
    
    for num in arr2:
        arrDict[num]+=1 
    
    for num in arr1: 
        if arrDict[num]==0: 
            return num 
        
        else: arrDict[num]-=1


def largest_cont_sum(arr):
    if len(arr)==0: 
        return 0
    
    max_sum=current_sum=arr[0] 
    
    for num in arr[1:]: 
        current_sum=max(current_sum+num, num)
        max_sum=max(current_sum, max_sum) 
        
    return max_sum


def reverse_words(str):
    arr = str.split()
    
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        right -=1
        left +=1
    
    
    print(arr)
    
def rev_word2(s):

    words = []
    length = len(s)
    spaces = [' ']
    
    i = 0
    
    while i < length:
        
        if s[i] not in spaces:
            
            word_start = i
            
            while i < length and s[i] not in spaces:
                
                i += 1
            words.append(s[word_start:i])
        i += 1
        
    return " ".join(reversed(words))  

def compress(strng):
    d = {}
     
    for letter in strng:
        if letter in d:
            d[letter] +=1
        else:
            d[letter] = 1
             
    result = ''
    for k in d:
        result += k 
        result += str(d[k])
        print(result)
      
    return result

def compress2(s):

    r = ""
    l = len(s)
    

    if l == 0:
        return ""
    
    if l == 1:
        return s + "1"

    last = s[0]
    cnt = 1
    i = 1
    
    while i < l:
        if s[i] == s[i - 1]: 
            cnt += 1
        else:
            r = r + s[i - 1] + str(cnt)
            cnt = 1
            
        i += 1
    
    r = r + s[i - 1] + str(cnt)
    
    return r

def unique_chars(string):
    
    seen = {}
    
    for letter in string:
        if letter in seen:
            return False
        else:
            seen[letter] = letter
    return True


    
    
if __name__ == '__main__': 
    amagram('god', 'dog') 
    #array_pair([1,3,2,2],4)
    
    #num = find_missing_number2([1,2,3,4,5,6,7],[3,7,2,1,4,6])
    #print(num)
    
    #largestNum = largest_cont_sum([1,2,-1,3,4,10,10,-10,-1])
    #print(largestNum)
    
    #reversedWords = reverse_words('tricks hat unassisted')
    #print(reversedWords)
    
    print(compress('AAAAABBBBCCCC'))
    
    print(unique_chars('abcabc'))
    
    