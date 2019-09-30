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

    def insert():
        pass

    def print():
        pass

    def resize_array():
        pass

    def add_to_front():
        pass
