class DynamicArray:
    def __init__(self, capacity=0):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * capacity

    def append(self, value):
        if self.count >= self.capacity:
            self.resize_array()

        self.storage[self.count] = value
        self.count += 1

    def insert(self, value, index):
        if self.count >= self.capacity:
            self.resize_array

        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]

        self.storage[index] = value
        self.count += 1

    def remove(self, index):
        value = self.storage[index]
        for i in range(index, self.count - 1, 1):
            self.storage[i] = self.storage[i + 1]
        self.count -= 1
        return value

    def print():
        for value in self.storage:
            print(value)

    def resize_array():
        # double the capacity
        self.capacity *= 2
        # crate a new array called storage with elements containing None
        new_storage = [None] * self.capacity
        # loop through the old array self.count number of times
        for i in range(self.count):
            # assign the ith element from self.storage to new_storage
            new_storage[i] = self.storage[i]
        # assign self.storage to new_storage
        self.storage = new_storage

    def add_to_front(self, value):
        self.insert(value, 0)
