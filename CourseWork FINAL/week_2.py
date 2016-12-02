#Question 1
print("Question 1")
from math import sqrt

def perfect_square(num):
    
    lower_root = int(sqrt(num))
    upper_root = lower_root + 1
    lower_square = lower_root * lower_root
    upper_square = upper_root * upper_root
    
    answer = 0
    
    #returns the perfect square root of the perfect square
    if upper_square >= num:
        answer = lower_root * lower_root
        print(lower_root)
        print("the closest perfect square is " + str(answer))
    else:
        answer = upper_root * upper_root
        print(upper_root)
        print("the closest perfect square is " + str(answer))
    
    #the actaul perfect square
    
    
perfect_square(350)