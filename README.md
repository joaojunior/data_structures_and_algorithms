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

## 1.4 MaxHeap

For the complexity, `n` is the number of items in the Heap.
1. Time complexity:
    - Best case:
        - max_heapify: `O(1)`, here is when we need to look only in a level below `i`.
        - build_max_heap: `O(n)`, for each element from position `n // 2 - 1` to `0`, we need to call `max_heapify`.
    - Worst case:
        - max_heapify: `O(lgn)`, we need to look all levels from the root until leaves.
        - build_max_heap: `O(n)`, for each element from position `n // 2 - 1` to `0`, we need to call `max_heapify`.
2. Space Complexity: `O(n)`, `build_max_heap` create a max heap in place.

## 1.5 MinHeap

For the complexity, `n` is the number of items in the Heap.
1. Time complexity:
    - Best case:
        - min_heapify: `O(1)`, here is when we need to look only in a level below `i`.
        - build_min_heap: `O(n)`, for each element from position `n // 2 - 1` to `0`, we need to call `min_heapify`.
    - Worst case:
        - min_heapify: `O(lgn)`, we need to look all levels from the root until leaves.
        - build_min_heap: `O(n)`, for each element from position `n // 2 - 1` to `0`, we need to call `min_heapify`.
2. Space Complexity: `O(n)`, `build_min_heap` create a min heap in place.

## 1.6 BinarySearchTree

For the complexity, `n` is the number of items in the Binary search tree and `h` is the tree's height.
1. Time complexity: In the worst case, `h = n`, the binary search tree is like a linked list.
    - search: `O(h)`, we do a binary search to find an element.
    - insert: `O(h)`, Either we need to find the element in the tree or we need to find the correct place for the new element. Both start in the tree's root and do a binary search.
    - delete: `O(h)`, We need to find the element in the tree and delete it. To find the element, we use the `search` method.

2. Space Complexity: `O(n)`


# 2. Algorithms
## Sorting 2.1
Here, `n` is the number of items to be sorted. Also, the videos below represent each algorithm in execution which red bars represent comparations.

### 2.1.1 SelectSort
- Time complexity:
    - Best case and Worst case:
        - `O(n^2)`, we select an `i th` item and compare it with all `j th` items, where `i < j < n`

![Select sort in an array asc sorted](https://user-images.githubusercontent.com/1184288/111559169-6cff0b80-8766-11eb-8dbf-c19c0f93a556.gif)
![Select sort in an array desc sorted](https://user-images.githubusercontent.com/1184288/111559392-ccf5b200-8766-11eb-89eb-7f9356614f55.gif)


- Space Complexity: `O(n)`

### 2.1.2 InsertSort
- Time complexity:
    - Best case:
        - `O(n)`, The array is already sorted in an ascending way and it is necessary doing only one comparison in the inner loop for each element of the array.
        ![Insert sort in an array asc sorted](https://user-images.githubusercontent.com/1184288/111558349-fb728d80-8764-11eb-94a8-7debe0d7f1f9.gif)
    - Worst case:
        - `O(n^2)`, The array is sorted in an descending way and it is necessary doing `i` comparison and changes in the inner loop for each element of the array.
        ![Insert sort in an array desc sorted](https://user-images.githubusercontent.com/1184288/111557948-1e507200-8764-11eb-8118-073276d541aa.gif)
- Space Complexity: `O(n)`

### 2.1.3 ShellSort
- Time complexity:
    - Best case:
        - `O(n*lgn)`, The array is already sorted in an ascending way and it is necessary doing only one comparison in the inner loop for each element of the array.
        ![out](https://user-images.githubusercontent.com/1184288/112078390-b7143280-8b54-11eb-8917-6ad4656ef209.gif)
    - Worst case:
        - `O(n^1.5)`, The array is sorted in an descending way.
        ![out](https://user-images.githubusercontent.com/1184288/112078292-8207e000-8b54-11eb-8c25-779c84541feb.gif)
- Space Complexity: `O(n)`

## 2.2 Tree traversal
Here, `n` is the number of nodes and `h` is the height of the Tree.

### 2.2.1 In-Order
- Time complexity: `O(n)`, we always need to visit each node of the tree.
- Space complexity: `O(h)`, we are using a recursive algorithm and `h` is the height of the tree recursive call.

### 2.2.2 Pre-Order
- Time complexity: `O(n)`, we always need to visit each node of the tree.
- Space complexity: `O(h)`, we are using a recursive algorithm and `h` is the height of the tree recursive call.

### 2.2.3 Post-Order
- Time complexity: `O(n)`, we always need to visit each node of the tree.
- Space complexity: `O(h)`, we are using a recursive algorithm and `h` is the height of the tree recursive call.
