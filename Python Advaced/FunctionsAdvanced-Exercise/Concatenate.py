def concatenate(*args, **kwargs):
    result = ''
    for s in args:
        result += s
    for k in kwargs:
        if k in result:
            k_in_result = result.count(k)
            result = result.replace(k, kwargs[k], k_in_result)
    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
