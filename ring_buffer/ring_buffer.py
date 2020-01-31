from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
         
        # check if at capacity
        if self.storage.length == self.capacity:
            
            # check that current position exists and its previous node is not the head
            if self.current and self.current is not self.storage.head:
                
                # replace value of previous node with item being appended 
                self.current.prev.value = item
                
                # update current node prosition 
                self.current = self.current.prev
            else:
                # remove previous tail
                self.storage.remove_from_tail()

                # add the new tail 
                self.storage.add_to_tail(item)
                
                # assign current to new tail 
                self.current = self.storage.tail

        else:
            # reached capacity so add item to head 
            self.storage.add_to_head(item)
       

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        
        # start at tail 
        current_node = self.storage.tail

        # loop through doubly linked list 
        for node in range(self.storage.length):
            
            # add the current value
            list_buffer_contents.append(current_node.value)

            # move to previous value 
            if current_node.prev:
                current_node = current_node.prev
        
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current = 0

    def append(self, item):
        # add new item at current index 
        self.storage[self.current] = item
        self.current += 1
    
        # reset the current index when at capacity 
        if self.current == self.capacity:
            self.current = 0

    def get(self):
        # filter out None and return values 
        return [item for item in self.storage if item is not None]