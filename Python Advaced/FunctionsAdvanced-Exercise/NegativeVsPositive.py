def get_positives_only(nums):
    result = []
    for num in nums:
        if num > 0:
            result.append(num)
    return result


def get_negatives_only(nums):
    result = []
    for num in nums:
        if num < 0:
            result.append(num)
    return result


numbers = [int(x) for x in input().split(' ')]
positives = get_positives_only(numbers)
negatives = get_negatives_only(numbers)
negativesSum = sum(negatives)
positivesSum = sum(positives)

print(negativesSum)
print(positivesSum)

if abs(negativesSum) > positivesSum:
    print("The negatives are stronger than the positives")
elif abs(negativesSum) < positivesSum:
    print("The positives are stronger than the negatives")
