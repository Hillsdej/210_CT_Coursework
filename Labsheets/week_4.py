sortedSeq = [1,3,5,6,17,29,30,42]

"""
def binary_search(s, target):
   
   low_index = 0
   high_index = len(s)
   
   while low_index <= high_index:
      middle = low_index + (high_index-low_index)//2
      
      if s[middle] == target:
         print("found")
         print(middle)
         break
      elif s[middle] < target: 
         low_index = middle + 1
      else:
         high_index = middle - 1

binary_search(sortedSeq,30)
"""
def binary_search2(s,u,l):
    
    low_index = 0
    high_index = len(s)
    middle = low_index + (high_index-low_index)//2
    
    while low_index <= high_index:
        if s[middle] <= u and s[middle] >= l:
            print("True")
            break
        elif s[middle] < l: 
            low_index = middle + 1
        else:
            high_index = middle - 1
    
    
binary_search2(sortedSeq,100,6)

