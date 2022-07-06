def sum_array(array, idx):
    if idx == len(array) - 1:
        return array[idx]
    return array[idx] + sum_array(array, idx+1)


array = [int(x) for x in input().split(' ')]
print(sum_array(array, 0))
