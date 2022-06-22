def stock_availability(inventory, command, *args):
    if command == 'delivery':
        boxes = list(args)
        inventory += boxes
    elif command == 'sell':
        values = list(args)
        if len(values) == 0:
            inventory.pop(0)
        elif len(values) == 1:
            try:
                num = int(values[0])
                for _ in range(num):
                    inventory.pop(0)
            except:
                if values[0] in inventory:
                    count = inventory.count(values[0])
                    for _ in range(count):
                        inventory.remove(values[0])
        else:
            for value in values:
                if value in inventory:
                    count = inventory.count(value)
                    for _ in range(count):
                        inventory.remove(value)

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
