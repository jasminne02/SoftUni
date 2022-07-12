def insertion_sort(array):
    for idx in range(len(array)):
        j = idx
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array


array = list(map(int, input().split(' ')))
array = insertion_sort(array)
print(" ".join(list(map(str, array))))
