from typing import List


class SelectSort():
    def sort(self, items: List) -> None:
        size = len(items)
        for i in range(size):
            index_min = i
            for j in range(i + 1, size):
                if items[j] < items[index_min]:
                    index_min = j
            items[i], items[index_min] = items[index_min], items[i]
