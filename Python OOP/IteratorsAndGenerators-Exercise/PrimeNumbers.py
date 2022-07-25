def get_primes(integers: list):
    for num in integers:
        prime = True
        if num <= 1:
            continue
        for n in range(2, num):
            if num % n == 0:
                prime = False
                break
        if prime:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
