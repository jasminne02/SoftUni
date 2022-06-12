def age_assignment(*args, **kwargs):
    result = dict()
    for name in args:
        first_letter = name[0]
        result[name] = kwargs[first_letter]

    result = sorted(result.items(),key=lambda x: x[0])
    result = [f'{k} is {v} years old.' for k, v in result]
    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print()
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
