import sys


class CustomList:
    def __init__(self):
        self.__list = []

    def append(self, value):
        self.__list.append(value)
        return self.__list

    def remove(self, index):
        self.__list.pop(index)
        return self.__list

    def get(self, index):
        return self.__list[index]

    def extend(self, iterable):
        self.__list += iterable
        return self.__list

    def insert(self, index, value):
        self.__list.insert(index, value)
        return self.__list

    def pop(self):
        return self.__list.pop()

    def clear(self):
        self.__list = []

    def index(self, value):
        for idx in range(len(self.__list)):
            if self.__list[idx] == value:
                return idx

    def count(self, value):
        count = 0
        for element in self.__list:
            if element == value:
                count += 1
        return count

    def reverse(self):
        return self.__list.reverse()

    def copy(self):
        return self.copy()

    def size(self):
        return len(self.__list)

    def add_first(self, value):
        self.__list.insert(0, value)

    def dictionize(self):
        dictionary = {}
        for idx in range(0, len(self.__list), 2):
            dictionary[idx] = self.__list[idx+1]
        return dictionary

    def move(self, amount):
        for _ in range(amount):
            element = self.__list.pop(0)
            self.__list.append(element)
        return self.__list

    def sum(self):
        list_sum = 0
        for element in self.__list:
            if element.isdigit():
                list_sum += float(element)
                continue
            list_sum += len(element)
        return list_sum

    def overbound(self):
        biggest_idx = 0
        biggest_element = -sys.maxsize
        for idx in range(len(self.__list)):
            element = self.__list[idx]
            if element.isdigit():
                if element > biggest_element:
                    biggest_idx = idx
                continue
            if len(element) > biggest_element:
                biggest_idx = idx
        return biggest_idx

    def underbound(self):
        smallest_idx = 0
        smallest_element = -sys.maxsize
        for idx in range(len(self.__list)):
            element = self.__list[idx]
            if element.isdigit():
                if element > smallest_element:
                    smallest_idx = idx
                continue
            if len(element) > smallest_element:
                smallest_idx = idx
        return smallest_idx
    