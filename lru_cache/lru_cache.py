import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

'''
Some questions;
    SO I didn't create a stack class...but since I'm adding/removing from the DLL tail, does that mean I still made a stack data structure anyway? Or is there something I'm missing?
'''


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
        self.cache_in_order = {}
        self.cache = DoublyLinkedList()
        #Honestly these variable names should be switched...the DLL is ordered, the dictionary is not.

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
            if temp == self.cache_in_order[temp]:
                self.set(key, self.cache_in_order[temp])
                return self.cache_in_order[temp]
            print(self.cache_in_order)
            # if str(key) == temp.value[0]:
            #     self.set(key, temp.value[1])
            #     return temp.value[1]
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
            self.cache_in_order[temp] = value
            # self.cache_in_order[key] = value
            #^how do I deal with the case where a pointer's key is None?
            return self.cache.add_to_tail((key, value))
        elif temp:
            while temp.prev is not None:
                if str(key) == temp.value[0]:
                    temp.delete()
                    overwrite = 1
                    self.cache_in_order[temp] = value
                    # self.cache_in_order[key] = value
                    return self.cache.add_to_tail((key, value))
                temp = temp.prev

        # #If limit will be exceeded and this is not an overwrite, delete oldest entry and add newest.
        if self.cache.length == self.limit and overwrite == 0:
            self.cache.delete(self.cache.head)
            self.cache_in_order[temp] = value
            # self.cache_in_order[key] = value
            return self.cache.add_to_tail((key, value))
        else:
            self.cache_in_order[temp] = value
            # self.cache_in_order[key] = value
            return self.cache.add_to_tail((key, value))

        if self.current_nodes != self.limit and overwrite == 0:
            self.current_nodes += 1