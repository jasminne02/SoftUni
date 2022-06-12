def even_odd_filter(**kwargs):
    to_return = {}
    for command, nums in kwargs.items():
        result = []
        if command == 'even':
            for n in nums:
                if n % 2 == 0:
                    result.append(n)
        elif command == 'odd':
            for n in nums:
                if n % 2 != 0:
                    result.append(n)
        to_return[command] = result

    to_return = sorted(
        to_return.items(),
        key=lambda x: (-len(x[1]))
    )
    return dict(to_return)


print(even_odd_filter(

    odd=[1, 2, 3, 4, 10, 5],

    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],

))
