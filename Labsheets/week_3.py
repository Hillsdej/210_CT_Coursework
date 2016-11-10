#Question 1
print("Question 1")

rArray = []
sentence = "this is just a test"
sArray = sentence.split()

def reverse2(x):
    
    if x >= 0:
        rArray.append(sArray[x])
        reverse2(x-1)
    else:    
        reverse = " ".join(rArray)
        print(reverse)
    
reverse2(len(sArray)-1)

    
"""
#Question 2
print ("Question 2")

def primeCheck(x,y):
    
    #y must be 1 less than x for this to work properly
    
    if y <= 1:
        print("x is a prime")    
    else:
        if x % y == 0:
            print("x is not prime")
        else:
            primeCheck(x,y-1)

primeCheck(11,10)


#Question 3
print("Question 3")
word = "cantelope"
wordList = list(word)

def vowelRemoval(step):
    
    #cannot remove more of the same vowel atm
    
    v = ["a","e","i","o","u"]
    
    if step < len(v):
        
        if v[step] in wordList:
            wordList.remove(v[step])
            print(wordList)
            vowelRemoval(step+1)
        else:
            vowelRemoval(step+1)
    
    else:
        updatedStr = " ".join(wordList)
        print(updatedStr)
    
    
    
    
vowelRemoval(0)
        
"""    


