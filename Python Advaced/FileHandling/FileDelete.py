import os

file = 'my_first_file.txt'
if os.path.exists(file):
    os.remove(file)
