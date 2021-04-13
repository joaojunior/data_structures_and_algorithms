from typing import List


class MinHeap():
    @classmethod
    def build_min_heap(cls: 'MinHeap', items: List):
        for i in range((len(items) - 1) // 2, -1, -1):
            cls.min_heapify(items, i)

    @classmethod
    def min_heapify(cls: 'MinHeap', items: List, i: int):
        left = 2 * i + 1
        right = left + 1
        size = len(items)
        j = i
        if left < size:
            if items[j] > items[left]:
                j = left
            if right < size and items[j] > items[right]:
                j = right
            if j != i:
                items[i], items[j] = items[j], items[i]
                cls.min_heapify(items, j)
