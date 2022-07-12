def selection_sort(array):
    for current_idx in range(len(array)):
        min_idx = current_idx
        min_element = array[min_idx]

        for idx in range(current_idx, len(array)):
            if array[idx] < min_element:
                min_idx = idx
                min_element = array[idx]

        if min_element < array[current_idx]:
            temp = array[current_idx]
            array[current_idx] = min_element
            array[min_idx] = temp
    return array


array = list(map(int, input().split(' ')))
array = selection_sort(array)
print(" ".join(list(map(str, array))))
