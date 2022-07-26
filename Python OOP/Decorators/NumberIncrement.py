def number_increment(numbers):

    def increase():
        for idx in range(len(numbers)):
            numbers[idx] += 1
        return numbers

    return increase()


print(number_increment([1, 2, 3]))

