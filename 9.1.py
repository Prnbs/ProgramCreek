class Stack:
    def __init__(self):
        self.data = None
        self.max = 0
        self.next = None
        self.head = None


    def push(self, data):
        new_item = Stack(data)
        new_item.next = self.head
        self.head = new_item
        new_item.max = max(self.max, data)


    def pop(self):
        if head is None:
            raise Exception('Nothing left to pop')

