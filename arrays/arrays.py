class DynamicArray:
    # initialize DynamicArray class with default of capacity 8
    def __init__(self, capacity=8):
        # how many elements are in the array
        self.count = 0
        # how many elements the array can hold
        self.capacity = capacity
        # reserver space in hardware and operating system memory
        self.storage = [None] * capacity

    def append(self, value):
        # if array is full, resize array
        if self.count >= self.capacity:
            self.resize_array()
        # add value to end of the array
        self.storage[self.count] = value
        # increment count
        self.count += 1

    # insert a value at a given index
    def insert(self, value, index):
        # check if there's space in storage
        if self.count >= self.capacity:
            self.resize_array

        # shift everything to the right of index to the right
        # starting from the rigt and move left to prevent overwriting values
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]

        # insert value into index
        self.storage[index] = value
        # increment count
        self.count += 1

    def remove(self, index):
        value = self.storage[index]
        for i in range(index, self.count - 1, 1):
            self.storage[i] = self.storage[i + 1]
        self.count -= 1
        return value

    def print(self):
        for value in self.storage:
            print(value)

    def resize_array(self):
        # double the capacity
        self.capacity *= 2
        # crate a new array called new_storage with self.capacity number of elements with the value set to None
        new_storage = [None] * self.capacity

        # copy old items into new_storage by looping through the old array self.count number of times
        for i in range(self.count):
            # assign the ith element from self.storage to new_storage
            new_storage[i] = self.storage[i]
        # assign self.storage to new_storage
        self.storage = new_storage

    def add_to_front(self, value):
        self.insert(value, 0)


arr = DynamicArray(8)
print(arr.storage)
arr.insert(0, "z")
arr.insert(0, "y")
arr.insert(0, "x")
arr.insert(0, "w")
print(arr.storage)
arr.append("a")
arr.append("b")
arr.append("c")
arr.append("d")
