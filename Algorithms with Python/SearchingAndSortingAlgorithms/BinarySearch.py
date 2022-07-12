def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_element = array[mid_idx]

        if mid_element == target:
            return mid_idx

        if mid_element < target:
            left = mid_element + 1
        elif mid_element > target:
            right = mid_element - 1

    return -1


array = list(map(int, input().split(' ')))
target = int(input())
print(binary_search(array, target))
