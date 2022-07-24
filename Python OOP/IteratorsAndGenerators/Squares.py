def squares(n):
    num = 1
    while num <= n:
        yield num * num
        num += 1


print(list(squares(5)))
