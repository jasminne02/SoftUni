def fibonacci():
    prev_number = 0
    current_num = 1
    yield prev_number
    yield current_num
    while True:
        num = prev_number + current_num
        prev_number = current_num
        current_num = num
        yield num


generator = fibonacci()
for i in range(5):
    print(next(generator))

print()

generator = fibonacci()
for i in range(1):
    print(next(generator))
