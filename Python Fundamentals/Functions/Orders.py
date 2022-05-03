product_input = input()
quantity_input = int(input())


def calculates(product, quantity):
    total_price = 0

    if product == 'coffee':
        total_price = 1.5 * quantity
    elif product == 'coke':
        total_price = 1.4 * quantity
    elif product == 'water':
        total_price = 1 * quantity
    elif product == 'snacks':
        total_price = 2 * quantity

    return total_price


print(f'{calculates(product_input, quantity_input):.2f}')
