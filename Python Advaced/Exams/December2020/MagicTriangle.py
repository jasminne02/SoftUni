def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for rowIdx in range(3, n+1):
        row = []
        colCounter = 0

        if rowIdx == 3:
            row = [1, 2, 1]
        else:
            for idx in range(rowIdx):
                if idx == 0 or idx == rowIdx - 1:
                    row.append(1)
                else:
                    x = triangle[rowIdx - 2][colCounter]
                    x += triangle[rowIdx - 2][colCounter + 1]
                    row.append(x)
                    colCounter += 1

        triangle.append(row)

    return triangle


get_magic_triangle(5)
