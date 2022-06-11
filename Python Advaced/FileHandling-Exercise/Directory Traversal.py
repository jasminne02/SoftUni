from os import listdir
from os.path import isdir, join


def directory_traversal(path, files_by_exit):
    for element in listdir(path):
        if isdir(join(path, element)):
            directory_traversal(join(path, element), files_by_exit)
        else:
            extension = element.split('.')[-1]
            if extension not in files_by_exit:
                files_by_exit[extension] = []
            files_by_exit[extension].append(element)


result = {}
directory_traversal('./', result)

for key, value in result.items():
    print(key, value)
