def reverse(idx, elements):
    if idx == len(elements) // 2:
        return
    swap_idx = len(elements) - 1 - idx
    elements[idx], elements[swap_idx] = elements[swap_idx], elements[idx]
    reverse(idx+1, elements)


elements = input().split()
reverse(0, elements)
print(" ".join(elements))
