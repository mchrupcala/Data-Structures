Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
    O(1), constant time, because a linked list's tail can be access directly so we don't have to traverse the list.

2. What is the runtime complexity of `dequeue`?
    O(1), constant time, because a linked list's head can be access directly so we don't have to traverse the list.

3. What is the runtime complexity of `len`?
    O(1) since it's just accessing a stored value/property.


## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
    O(n) - we have to assume the node being added is one of the last entries in the list.

2. What is the runtime complexity of `ListNode.insert_before`?
    O(n) - we have to assume the node being added is one of the middle/last entries in the list.

3. What is the runtime complexity of `ListNode.delete`?
    O(1)? Seems like this would be called with a direct reference to the node being deleted.

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
    O(n) - we can directly access a Linked list's head.

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
    O(n) - we can directly access a Linked list's head.

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
    O(n) - we can directly access a Linked list's tail.

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
    O(n) - we can directly access a Linked list's tail.

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
    O(n) assuming that we're traversing the majority of the list.

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
    O(n) assuming that we're traversing the majority of the list.

10. What is the runtime complexity of `DoublyLinkedList.delete`?
    O(1) - even though there's a few conditionals, we ignore coefficients and heads/tails can be accessed directly.

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
        array.splice - O(n), linkedList.delete() - O(1)