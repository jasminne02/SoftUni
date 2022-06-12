def fill_the_box(*args):
    height, length, width, *cubes = args
    box_capacity = height * length * width
    for i in range(3, len(args)):
        box = args[i]
        if box == 'Finish':
            break
        box_capacity -= box

    if box_capacity < 0:
        return f"No more free space! You have {abs(box_capacity)} more cubes."
    elif box_capacity > 0:
        return f"There is free space in the box. You could put {box_capacity} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
