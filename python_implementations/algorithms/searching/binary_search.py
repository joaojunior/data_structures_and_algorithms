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


def binary_search_less_than(item, items):
    left = 0
    right = len(items) - 1
    idx = -1
    while left <= right:
        mid = left + (right - left) // 2
        if items[mid] < item:
            idx = mid
            left = mid + 1
        else:
            right = mid - 1
    return idx


def binary_search_bigger_than(item, items):
    left = 0
    right = len(items) - 1
    idx = -1
    while left <= right:
        mid = left + (right - left) // 2
        if items[mid] > item:
            idx = mid
            right = mid - 1
        else:
            left += 1
    return idx


def binary_search_rotate_array_index_min(items):
    if len(items) == 0:
        return -1
    left = 0
    right = len(items) - 1
    while left < right:
        mid = left + (right - left) // 2
        if items[mid] < items[right]:
            right = mid
        else:
            left = mid + 1
    return left
