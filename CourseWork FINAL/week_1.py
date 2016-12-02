#Question 1
print("Question 1")                                                 #O(1)   
"""
could import random
random integer for index

"""
import random

def random_sort():
    
    array = []                                                      #O(1)
    
    #generate random numbers for List
    
    for num in range(0,10):
        x = random.randint(0,100)                                   #O(n)
        array.append(x)                                             #O(n)
        
    print("This is the original array: ")                           #O(1)
    print(array)                                                    #O(1)

    arrayLength = len(array)                                        #O(1)
    
    associationA = [0,1,2,3,4]                                      #O(1)
    assosciationB = [5,6,7,8,9]                                     #O(1)
    
    
    for num in range(0,arrayLength):
        z = random.randint(0,arrayLength-1)                         #O(n)
        a = random.choice(associationA)                             #O(n)
        b = random.choice(assosciationB)                            #O(n)
        array[a],array[z] = array[z], array[a]                      #O(n)
        array[0],array[b] = array[b], array[0]                      #O(n)
        
    
    print("This is the new array: ")                                #O(1)
    
    print(array)                                                    #O(1)

random_sort()                                                       #O(1)

#Has a worst case efficiency of O(n)

#Question 2 
print("Question 2")                                                 #O(1)
"""
a factorial is the multiplication of its descending natural numbers
e.g. 4! == 4*3*2*1 == 24
"""
#Reference material http://www.purplemath.com/modules/factzero.htm


def zeroTrail(f):
    
    #get a list of the factors
    factorials = []                                                #O(1)
    for num in range(0,f):                                         #O(n)
        factorials.append(f)                                       #O(n)
        f -= 1                                                     #O(n)
    
    #print(factorials)
    
    total = 1                                                      #O(1)
    
    #iterate through the list and multiply to get the factorial number
    for num in factorials:                                         #O(n)
        total *= num                                               #O(n)
    
    #print(total)
    
    #stores how many 5's in the factorial total 
    store = []                                                     #O(1)

    y = len(factorials) // 5                                       #O(1)               
    store.append(y)                                                #O(1)
    
    while True:                                                    #O(n)
        y = y // 5                                                 #O(n)
        if y < 1:                                                  #O(n)
            break                                                  #O(n)
        else:                                                      #O(n)  
            store.append(y)                                        #O(n)
    
    
    
    #print(store)
    totalZero = sum(store[0:len(store)])                           #O(1)
    
    print("The number of trailing zero's in this factorial number is: " + str(totalZero))   #O[1]
    
zeroTrail(1000)                                                    #(1)

#Has a worst case efficiency of O(n)

#Question 3

"""
a. Does your algorithm have defined inputs and outputs?
    
    for Question 1 they are defined but I could increase the range of the numbers used in the random generator
    for Question 2 the input is user defined

b. Can you guarantee that it terminates?
    
    yes 
    
c. Is it specified in a clear and concise manner?

    yes
    
d. Does your algorithm produce the correct result for all instances?

    yes
"""
