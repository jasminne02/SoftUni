def best_list_pureness(*args):
    numList, numK = args
    numList = [int(x) for x in numList]
    numK = int(numK)

    bestPurness = 0
    rotations = 0

    for r in range(0, numK):
        currentPurness = 0

        for idx in range(len(numList)):
            currentPurness += (numList[idx] * idx)

        if currentPurness > bestPurness:
            bestPurness = currentPurness
            rotations = r

        x = numList.pop()
        numList.insert(0, x)

    return f"Best pureness {bestPurness} after {rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
