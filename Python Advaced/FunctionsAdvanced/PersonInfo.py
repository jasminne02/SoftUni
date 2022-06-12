def get_info(name, age, town):
    return f"This is {name} from {town} and she is {age} years old"


person = {'age': 20, 'name': 'Jasmine', 'town': 'Plovdiv'}
print(get_info(**person))
