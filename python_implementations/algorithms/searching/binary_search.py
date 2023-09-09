def binary_search(item, items):
    left = 0
    right = len(items) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if items[mid] == item:
            return mid
        elif items[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    return -1
