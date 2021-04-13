from typing import List


class MaxHeap:
    @classmethod
    def build_max_heap(cls: 'MaxHeap', items: List):
        for i in range((len(items) - 1) // 2, -1, -1):
            cls.max_heapify(items, i)

    @classmethod
    def max_heapify(cls: 'MaxHeap', items: List, i: int):
        left = i * 2 + 1
        right = left + 1
        size = len(items)
        if left < size:
            j = i
            if items[j] < items[left]:
                j = left
            if right < size and items[j] < items[right]:
                j = right
            if j != i:
                items[i], items[j] = items[j], items[i]
                cls.max_heapify(items, j)
