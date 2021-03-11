[![codecov](https://codecov.io/gh/joaojunior/data_structures_and_algorithms/branch/main/graph/badge.svg?token=8G2K2F71JB)](https://codecov.io/gh/joaojunior/data_structures_and_algorithms)

# 1. Data Structure
## 1.1 Linked List

For the complexity, `n` is the number of items in the LinkedList.
1. Time complexity:
    - Best case:
        - Insert: `O(1)`, we always insert a new item in front of the LinkedList.
        - Delete: `O(1)`, the item to delete is the first element of the LinkedList.
    - Worst case:
        - Insert: `O(1)`, we always insert a new item in front of the LinkedList.
        - Delete: `O(n)`, the item to delete is the last element of the LinkedList.

2. Space Complexity: `O(n)`

## 1.2 Stack

For the complexity, `n` is the number of items in the Stack. Also, this implementation use the LinkedList to store items.
1. Time complexity:
    - Best case:
        - Push: `O(1)`, we always insert a new item in front of the LinkedList.
        - Pop: `O(1)`, the item to delete is the first element of the LinkedList.
    - Worst case:
        - Push: `O(1)`, we always insert a new item in front of the LinkedList.
        - Pop: `O(1)`, the item to delete is always the first element of the LinkedList.

2. Space Complexity: `O(n)`

## 1.3 Queue

For the complexity, `n` is the number of items in the Queue. Also, this implementation use the LinkedList to store items. This LinkedList always insert an element in the end of the list. To do this operation in `O(1)`, the list keep a pointer to the last element of the list.
1. Time complexity:
    - Best case:
        - Enqueue: `O(1)`, we always insert a new item after the last element of the LinkedList that has a pointer to it last element.
        - Dequeue: `O(1)`, the item to delete is the first element of the LinkedList.
    - Worst case:
        - Enqueue: `O(1)`, we always insert a new item after the last element of the LinkedList that has a pointer to it last element.
        - Dequeue: `O(1)`, the item to delete is the first element of the LinkedList.

2. Space Complexity: `O(n)`


# 2. Algorithms
## Sorting 2.1
Here, `n` is the number of items to be sorted.

### 2.1.1 SelectSort
- Time complexity:
    - Best case and Worst case:
        - `O(n^2)`, we select an `i th` item and compare it with all `j th` items, where `i < j < n`
- Space Complexity: `O(n)`

### 2.1.2 InsertSort
- Time complexity:
    - Best case:
        - `O(n)`, The array is already sorted in an ascending way and it is necessary doing only one comparison in the inner loop for each element of the array.
    - Worst case:
        - `O(n^2)`, The array is sorted in an descending way and it is necessary doing `i` comparison and changes in the inner loop for each element of the array.
- Space Complexity: `O(n)`
