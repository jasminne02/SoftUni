listInput = input().split(' ')
productsToSearchFor = input().split(' ')
productsDic = {}

for index in range(0, len(listInput), 2):
    productsDic[listInput[index]] = int(listInput[index+1])

for searched in productsToSearchFor:
    if searched in productsDic.keys():
        print(f'We have {productsDic[searched]} of {searched} left')
    else:
        print(f'Sorry, we don\'t have {searched}')
