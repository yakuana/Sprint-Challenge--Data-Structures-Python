class BinarySearchTree:                              # worst case O(n), average case O(log n)
    def __init__(self, value):                       # restricting the input value to a number
        self.value = value
        self.left = None                             # use to traverse left ==> pointers
        self.right = None                            # use to traverse right ==> pointers

    def __repr__(self):
        return (f"Value= {self.value}, Left: {self.left}, Right: {self.right}")

    # Insert the given value into the tree
    def insert(self, value):
        if  self.value > value:                       
            if self.left == None:                     
                 self.left = BinarySearchTree(value)  
            else:
                self.left.insert(value)        

        if  self.value <= value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value) 

    # Returns True if the tree contains the value
    def contains(self, target):
        if target == self.value:                    
            return True                             
        elif target > self.value:                    
            if self.right != None:                  
                return self.right.contains(target)   
            else:                                   
                    return False                    

        elif target < self.value:                   
            if self.left != None:                   
                return self.left.contains(target)    
            else:                                   
                return False 

    # Return the maximum value found in the tree
    def get_max(self):

        if self.right != None:                        
            return self.right.get_max()               
        else:
            return self.value                         

    # Search each node in entire tree
    def for_each(self, cb):                          
        cb(self.value)                                 
        if self.right:                                 
            self.right.for_each(cb)
        if self.left:                                  
            self.left.for_each(cb)