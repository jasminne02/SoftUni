command = input().split('|')
numList = list()

for i in range(len(command) - 1, -1, -1):
    nums = [int(x) for x in command[i].split(' ') if x != ' ' and x != '']
    numList.append(nums)

numList = [num for sublist in numList for num in sublist]
for num in numList:
    print(num, end=' ')
