#Question 1

#Tests
#seq = [1,2,3,4,1,5,1,6,7]
#seq = [5,3,2,4,6,7,3,9]
seq = [5,4,3,2,1,6,7,8,5,6,8,9,13,22]

def largest_seq(seq):
    
    """
    function that takes in an array of numbers and
    outputs the sub sequence of ascending numbers of maximum length
    """ 
    #Set positional variable to reference index when iterating through sequence
    x = 0
    
    #Set counter variable which will increment for the length of a potential substring
    counter = 1
    
    #Create empty list to store counter variables for reference later
    counterList = [] 
    
    #Iterate through sequence and increment counter
    for x in range(0,len(seq)-1):
        
        #Condition to check if current element is less than the next
        if seq[x] < seq[x+1]:
            
            counter += 1
            x += 1
            
        else:
            
            counterList.append(counter)
            #reset counter
            counter = 1
            x += 1
           
    counterList.append(counter)
    print("this is the counterList: " + str(counterList))
    
    #set another positional variable for referencing index in counterList
    y = 0
    
    #set bounds for extracting sub_sequence
    z = 0
    a = 0 
    
    #Find the counter of max value
    highestCounter = max(counterList)
    
    #iterate through the counter list to find the position of the maximum element
    
    while y in range(0,len(counterList)-1):
        
        #Condition to check if the current element is the maximum element
        if counterList[y] == highestCounter:
            
            #If the maximum element is in position 0 then return the sequence from 0 up until the value stored in the counterList at index 0
            if y == 0:
                print("this is the sub_sequence: " + str(seq[0:counterList[y]]))
                break
            elif y == 1:
                #If the maximum element is at position 1, start from the previous elements value and finish at the current elements value
                print("this is the sub_sequence: " + str(seq[counterList[y-1]:counterList[y]]))
                break
            else:
                #if the maximum element is at position 2 or more, find the sum of all the previous elements up to but not including the current element to start
                #finish at the sum of all the previous elements including the current element
                a = sum(counterList[0:y])
                z = sum(counterList[0:y+1])
                print("this is the sub_sequence: " + str(seq[a:z]))
                break
        else:
            y +=1
    
    #If the maximum element is the last element in the counterList
    if y == len(counterList)-1:
        a = sum(counterList[0:y])
        z = sum(counterList[0:y+1])
        print("this is the sub_sequence: " + str(seq[a:z]))
            
largest_seq(seq)



class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None

class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          #Not actually perfect: how do we prepend to an existing list?
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x

#ADDED A DELETE METHOD      
      def delete(self,del_nodeVal):
        
        startingNode = self.head

        while startingNode != None:
            
            if startingNode.value == del_nodeVal:
                #is starting nodes value is equal to the value you want to delete
                
                if startingNode.prev != None:
                    #if the previous pointer has a pointer
                    
                    startingNode.prev.next = startingNode.next
                    #update the node before the startingNodes' next pointer to point to the startingNodes next pointer 
                    
                    startingNode.next.prev = startingNode.prev
                    #update the next nodes previous pointer to point to the starting nodes previous pointer
                
                else:
                    #if there is no previous pointer set the head to be the next pointer of the startingNode
                    #and set the starting nodes previous pointer to none
                    
                    self.head = startingNode.next
                    startingNode.next.prev = None
            
            startingNode = startingNode.next
            
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List: ",",".join(values))
          
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(2))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.delete(6)
    l.delete(8)
    l.display()