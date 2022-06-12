def math_operations(*args, **kwargs):
    count = 1
    for num in args:
        if count == 1:
            kwargs['a'] += num
        elif count == 2:
            kwargs['s'] -= num
        elif count == 3 and num != 0:
            kwargs['d'] /= num
        elif count == 4:
            kwargs['m'] *= num

        if count == len(kwargs):
            count = 1
        else:
            count += 1

    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    result = [f'{k}: {v:.1f}' for k, v in result]
    return '\n'.join(result)



print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print()
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(- 2.3), d=0, m=0))
print()
print(math_operations(6.0, a=0, s=0, d=5, m=0))
