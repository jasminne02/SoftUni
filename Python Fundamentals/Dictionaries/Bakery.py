stock = input().split(' ')
stockDic = {}

for index in range(0, len(stock), 2):
    stockDic[stock[index]] = int(stock[index + 1])

print(stockDic)
