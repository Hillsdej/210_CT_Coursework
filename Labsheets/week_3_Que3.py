print("Question 3")
word = "cantelope"
wordList = list(word)


def vowelRemoval(step):
    
    v = ["a","e","i","o","u"]
    
    if step < len(v):
        
        if v[step] in wordList:
            while v[step] in wordList:
                wordList.remove(v[step])
                vowelRemoval(step+1)
        else:
            vowelRemoval(step+1)
    
    else:
        updatedStr = " ".join(wordList)
        print(updatedStr)
    
    
    
    
vowelRemoval(0)
        