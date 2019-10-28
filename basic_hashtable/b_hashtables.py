# Basic hash table key/value pair
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# Basic hash table
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [Pair(None, None)] * capacity


# djb2 hash function
def hash(string, max):
    hash = 5381
    for char in string:
        # << shifts the bits of the first operand left by 5 bits
        # ord(char) is the numerical ascii value for every character in string
        hash = ((hash << 5) + hash) + ord(char)
    # returns a hashed integer between 0 and max
    return hash % max


def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)

    # if you are overwriting a value with a different key, print a warning.
    if hash_table.storage[index].value != None:
        print('Warning, overwriting existing data on insert')

    # create a new key/value pair
    hash_table.storage[index] = Pair(key, value)


def hash_table_remove(hash_table, key):
    # hash the key, max is hash table capacity
    index = hash(key, hash_table.capacity)

    # If you try to remove a value that isn't there, print a warning.
    if hash_table.storage[index].value == None or hash_table.storage[index].key != key:
        print(f"Warning: key: {key} does not exist")
    # else remove the key/value pair
    else:
        hash_table.storage[index] = Pair(None, None)


def hash_table_retrieve(hash_table, key):
    # unhash the key to get the index
    index = hash(key, hash_table.capacity)
    # if there is an element at the index and they have matching keys
    if hash_table.storage[index] is not None and hash_table.storage[index].key == key:
        return hash_table.storage[index].value
    else:
        # return None if the key is not found.
        return None


def Testing():
    ht = BasicHashTable(16)
    hash_table_insert(ht, "line", "Here today...\n")
    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
