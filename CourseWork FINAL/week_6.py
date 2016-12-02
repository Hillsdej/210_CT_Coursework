class BinTreeNode():
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 

def in_order(tree):
    
    #stack to store values
    tree_stack = []
    
    #if the stack was empty we would know it is finished
    empty = 0
    
    #this is the topmost/starting point
    cur_n = tree
  
    while True:
        
        #if the current node did = None then you know you've reached the leaf furthest on the left
        if cur_n != None:
            
            #put pointer to node into stack
            tree_stack.append(cur_n)
            
            #follow traversal down left side of tree
            cur_n = cur_n.left
            
        else:
            #go back to the start of the stack
            if len(tree_stack) != empty:
                
                #remove the top of the stack and print its value
                cur_n = tree_stack.pop()
                print(cur_n.value)
                
                #do the same for the right side
                cur_n = cur_n.right
                
            else:
                break
                
                
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  tree_insert(t,26)
  in_order(t)