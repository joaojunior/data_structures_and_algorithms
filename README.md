![Test Coverage](https://codecov.io/gh/joaojunior/data_structures_and_algorithms/branch/master/graph/badge.svg)

# Linked List

For the complexity, `n` is the number of items in the LinkedList.
1. Time complexity:
    - Best case:
        - Insert: `O(1)`, we always insert a new item in front of the LinkedList.
        - Delete: `O(1)`, the item to delete is the first element of the LinkedList.
    - Worst case:
        - Insert: `O(1)`, we always insert a new item in front of the LinkedList.
        - Delete: `O(n)`, the item to delete is the last element of the LinkedList.

2. Space Complexity: `O(n)`

# Stack

For the complexity, `n` is the number of items in the Stack. Also, this implementation use the LinkedList to store items.
1. Time complexity:
    - Best case:
        - Push: `O(1)`, we always insert a new item in front of the LinkedList.
        - Pop: `O(1)`, the item to delete is the first element of the LinkedList.
    - Worst case:
        - Push: `O(1)`, we always insert a new item in front of the LinkedList.
        - Pop: `O(1)`, the item to delete is always the first element of the LinkedList.

2. Space Complexity: `O(n)`

# Queue

For the complexity, `n` is the number of items in the Queue. Also, this implementation use the LinkedList to store items. This LinkedList always insert an element in the end of the list. To do this operation in `O(1)`, the list keep a pointer to the last element of the list.
1. Time complexity:
    - Best case:
        - Enqueue: `O(1)`, we always insert a new item after the last element of the LinkedList that has a pointer to it last element.
        - Dequeue: `O(1)`, the item to delete is the first element of the LinkedList.
    - Worst case:
        - Enqueue: `O(1)`, we always insert a new item after the last element of the LinkedList that has a pointer to it last element.
        - Dequeue: `O(1)`, the item to delete is the first element of the LinkedList.

2. Space Complexity: `O(n)`
