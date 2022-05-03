happiness = list(map(int, input().split(' ')))
factor = int(input())
happiness = [i * factor for i in happiness]

average = sum(happiness) / len(happiness)
half = [i for i in happiness if i >= average]

if len(half) >= len(happiness) // 2:
    print(f'Score: {len(half)}/{len(happiness)}. Employees are happy!')
else:
    print(f'Score: {len(half)}/{len(happiness)}. Employees are not happy!')
