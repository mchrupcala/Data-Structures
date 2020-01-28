import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of 
    1) the max number of nodes it can hold
    
    2) the current number of nodes it is holding
    
    3) a doubly- linked list that holds the key-value entries in the correct order
    
    4) a storage dict that provides fast access to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.current_nodes = 0
        self.cache_in_order = DoublyLinkedList()
        self.cache = DoublyLinkedList()

    """
    1) Retrieves the value associated with the given key. 
    
    2) Also needs to move the key-value pair to the end of the order such that the pair is considered most-recently used.
    
    3) Returns the value associated with the key or None if the key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        temp = self.cache.tail
        if temp is None:
            return None

        while temp is not None:
            if str(key) == temp.value[0]:
                self.set(key, temp.value[1])
                return temp.value[1]
            temp = temp.prev
        return 

    """
    1) Adds the given key-value pair to the cache. 
    
    2) The newly-added pair should be considered the most-recently used entry in the cache. 
    
    3) If the cache is already at max capacity before this entry is added, then the oldest entry in the cache needs to be removed to make room. 
    
    4) Additionally, in the case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with the newly-specified value.
    """
    def set(self, key, value):
        overwrite = 0
        temp = self.cache.tail
        if temp is None:
            return self.cache.add_to_tail((key, value))
        elif temp:
            while temp.prev is not None:
                if str(key) == temp.value[0]:
                    temp.delete()
                    overwrite = 1
                    return self.cache.add_to_tail((key, value))
                temp = temp.prev

        # #If limit will be exceeded and this is not an overwrite, delete oldest entry and add newest.
        if self.cache.length == self.limit and overwrite == 0:
            self.cache.delete(self.cache.head)
            return self.cache.add_to_tail((key, value))
        else:
            return self.cache.add_to_tail((key, value))

        if self.current_nodes != self.limit and overwrite == 0:
            self.current_nodes += 1