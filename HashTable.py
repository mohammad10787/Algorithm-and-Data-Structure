# defining the hash class

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return  h % 10

    # def add(self, key, val):
    #     h = 0
    #     h = self.get_hash(key)
    #     self.arr[h] = val
    #
    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

# instead of using get and add functions one can use python functions: __setitem__ and __getitem__ the same way as we
# defined the above functions. We have

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]

# Now we can use a different method to call these methods in the HashTable class

if __name__ == '__main__':
    t = HashTable()
    t['march 7'] = 130
    t['march 21'] = 20
    t['march 17'] = 39
    t['february 16'] = 50
    t['december 02'] = 10
    t['december 03'] = 15
    print(t.arr)
    print(t['march 17'])
    del(t['march 17'])
    print(t.arr)

# We defined a dictionary

