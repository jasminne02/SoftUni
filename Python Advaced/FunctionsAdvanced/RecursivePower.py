def recursive_power(num, power):
    result = 1
    if power == 0:
        return result
    result = num * recursive_power(num, power-1)
    return result


print(recursive_power(2, 10))
