class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


def detect_cycle(head):
    slow = head
    speedy = head.next
    cycle = False

    while head is not None:
        if slow == speedy:
            cycle = True
            break
        else:
            slow = slow.next
            if speedy is not None:
                speedy = speedy.next
            else:
                break
            if speedy is not None:
                speedy = speedy.next
            else:
                break

    return cycle

def create_list(data):
    head = LinkedListNode(data[0])
    save_the_head = head
    for i, item in enumerate(data[1:]):
        new_node = LinkedListNode(item)
        head.next = new_node
        head = head.next
    return save_the_head

def create_cycle(head):
    save_the_head = head

    while head.next is not None:
        head = head.next

    head.next = save_the_head
    return save_the_head

if __name__ == "__main__":
    head = create_list([1,2,3,4,5,6,7])
    head = create_cycle(head)

    print(detect_cycle(head))



