number = int(input())
studentInfo = dict()

for n in range(number):
    student = tuple(input().split(' '))
    name, grade = student

    if name not in studentInfo:
        studentInfo[name] = list()

    studentInfo[name].append(float(grade))

for name, grades in studentInfo.items():
    print(f'{name} -> ', end='')
    for grade in grades:
        print(f'{grade:.2f}', end=' ')
    print(f'(avg: {(sum(grades)/len(grades)):.2f})')
