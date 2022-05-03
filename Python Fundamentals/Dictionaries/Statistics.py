bakeryProducts = {}

while True:
    command = input()
    if command == 'statistics':
        break

    command = command.split(': ')
    key = command[0]
    value = int(command[1])

    if key in bakeryProducts:
        add = value + bakeryProducts.get(key)
        bakeryProducts[key] = add
    else:
        bakeryProducts[key] = value

print('Products in stock:')
for key in bakeryProducts.keys():
    print(f'- {key}: {bakeryProducts[key]}')
values = bakeryProducts.values()
print(f'Total Products: {len(bakeryProducts)}\nTotal Quantity: {sum(values)}')
