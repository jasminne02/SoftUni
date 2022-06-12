def sorting_cheeses(**kwargs):
    sortedCheese = sorted(
        kwargs.items(),
        key=lambda x: (-len(x[1]), x[0])
    )

    result = []

    for name, piecesCounts in sortedCheese:
        result.append(name)
        quantity = sorted(piecesCounts, reverse=True)
        result += quantity

    return '\n'.join([str(x) for x in result])


cheeses = {'Parmesan': [102, 120, 135], 'Camembert': [100, 100, 105, 430], 'Mozzarella': [50, 125]}
print(sorting_cheeses(**cheeses))
