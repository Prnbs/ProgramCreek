
class HashNode:
    def __init__(self, key, value):
        self.next_node = None
        self.key = key
        self.value = value

    def __str__(self):
        return self.key

    __repr__ = __str__


class HashMap:
    size = 23

    def __init__(self):
        self.l_main_list = [None] * self.size

    @staticmethod
    def is_numeric(key):
        try:
            float(key)
            return True
        except ValueError:
            return False

    @staticmethod
    def hashit(key):
        if HashMap.is_numeric(key):
            return key % HashMap.size
        else:
            char_sum = 0
            for char in key:
                char_sum += ord(char) - ord("a")
            return char_sum % HashMap.size

    def put(self, key, value):
        index = self.hashit(key)
        if self.l_main_list[index] is None:
            self.l_main_list[index] = HashNode(key, value)
        else:
            curr_node = self.l_main_list[index]
            while curr_node.next_node is not None:
                curr_node = curr_node.next_node
            curr_node.next_node = HashNode(key, value)

    def get(self, key):
        index = self.hashit(key)
        curr_node = self.l_main_list[index]
        if curr_node is None:
            return None
        if curr_node.key == key:
            return curr_node.value
        if curr_node.next_node is not None:
            while curr_node.next_node is not None:
                if curr_node.key == key:
                    return curr_node.value
                curr_node = curr_node.next_node
        # for last time in chain
        if curr_node.key == key:
            return curr_node.value
        else:
            return None

    def delete(self, key):
        index = self.hashit(key)
        curr_node = self.l_main_list[index]
        if curr_node is None:
            return True
        if curr_node.key == key:
            # no chains in this bin
            if curr_node.next_node is None:
                self.l_main_list[index] = None
                return True
            # this bin has chains
            self.l_main_list[index] = curr_node.next_node
            return True
        # key is inside a chain
        else:
            prev_node = curr_node
            curr_node = curr_node.next_node
            while curr_node.next_node is not None:
                if curr_node.key == key:
                    prev_node.next_node = curr_node.next_node
                    return True
                prev_node = curr_node
                curr_node = curr_node.next_node
            # last item
            if curr_node.key == key:
                prev_node.next_node = None
                return True
        return False


if __name__ == '__main__':
    hashmap = HashMap()
    hashmap.put("word", 3)
    hashmap.put("wrod", 5)
    hashmap.put("owrd", 6)
    print (hashmap.get("owrds"))
    print (hashmap.delete("word"))


