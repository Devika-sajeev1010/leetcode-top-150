import random

class RandomizedSet:

    def __init__(self):
        self.values = []       # stores elements
        self.index_map = {}    # stores element:index

    def insert(self, val):
        if val in self.index_map:
            return False

        self.values.append(val)
        self.index_map[val] = len(self.values) - 1

        return True

    def remove(self, val):
        if val not in self.index_map:
            return False

        # index of element to remove
        index = self.index_map[val]

        # last element in array
        last_element = self.values[-1]

        # move last element to deleted position
        self.values[index] = last_element
        self.index_map[last_element] = index

        # remove last element
        self.values.pop()

        # delete from hashmap
        del self.index_map[val]

        return True

    def getRandom(self):
        return random.choice(self.values)