def rec_sum(n):
    if n == 0:
        return 0
    
    return n + rec_sum(n-1)

def mod_sum(n):
    if n < 10:
        return int(n)
    else:
        return n%10 + mod_sum(int(n/10))
    
    
def word_split(phrase,list_of_words, output = None):
    if output is None:
        output = []
    
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            
            return word_split(phrase[len(word):],list_of_words,output)
    
    return output 
    
    
if __name__ == '__main__':
    #print(rec_sum(5))
    print(mod_sum(24666))
    print(word_split('themanran',['unassisted','the','ran','man']))