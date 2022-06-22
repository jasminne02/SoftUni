def start_spring(**kwargs):
    objects_dict = dict()
    objects = dict()
    final_objects = dict()
    to_return = ''

    for name, value in kwargs.items():
        objects_dict[name] = value

    for k, v in objects_dict.items():
        if v not in objects:
            objects[v] = []
        objects[v].append(k)

    objects = sorted(
        objects.items(),
        key=lambda x: (-len(x[1]), x[0])
    )

    for k, v in objects:
        v = sorted(v)
        final_objects[k] = v

    for k, l in final_objects.items():
        to_return += k + ":\n"
        for e in l:
            to_return += '-' + e + '\n'

    return to_return


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
print()

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
print()

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
print()
