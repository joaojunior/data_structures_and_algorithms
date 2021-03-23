from typing import List


class ShellSort:
    def sort(self, items: List) -> None:
        size = len(items)
        h = 1
        while h < size / 3:
            h = 3 * h + 1
        while h >= 1:
            for i in range(h, size):
                j = i
                while j >= h and items[j] < items[j-h]:
                    items[j-h], items[j] = items[j], items[j-h]
                    j -= h
            h = h // 3
