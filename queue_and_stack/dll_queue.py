import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        #   Because the pointers in a DLL give us a strict order to work with, so queues and stacks can remove/add from the head/tail pretty easily.
        # self.storage = ?

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass

    def len(self):
        pass
