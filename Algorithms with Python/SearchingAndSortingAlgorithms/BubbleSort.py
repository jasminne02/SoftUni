def bubble_sort(array):
    is_sorted = False
    i = 0
    while not is_sorted:
        is_sorted = True
        for idx in range(1, len(array) - i):
            if array[idx-1] > array[idx]:
                array[idx-1], array[idx] = array[idx], array[idx-1]
                is_sorted = False
        i += 1
    return array


array = list(map(int, input().split(' ')))
array = bubble_sort(array)
print(" ".join(list(map(str, array))))
