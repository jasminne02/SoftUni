def reverse_text(string: str):
    idx = len(string)-1

    while idx >= 0:
        yield string[idx]
        idx -= 1


for char in reverse_text("step"):
    print(char, end="")
