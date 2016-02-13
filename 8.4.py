
class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.jump = None
        self.next = next


def copy_basic_list(head):
    # create a new head
    new_head = LinkedListNode(head.data)
    save_the_head = new_head
    head = head.next
    while head is not None:
        # move original head
        # create a new empty node
        new_node = LinkedListNode(head.data)
        # point new head to this empty node
        new_head.next = new_node
        # move new head to this new node
        new_head = new_node
        head = head.next
    return save_the_head


def serialize_orig_list(head):
    '''Replace the data in the original list with sequential numbers'''
    count = 1
    save_the_head = head
    while head is not None:
        head.data = count
        count += 1
        head = head.next
    return save_the_head


def move_to_nth_node(head, node_number):
    count = 1
    while count < node_number:
        count += 1
        head = head.next
    return head


def copy_jumps(head, new_head):
    original_head = head
    original_new_head = new_head
    iterator = head
    iterator_copy = new_head
    save_the_head = new_head

    while iterator is not None:
        jumped_node = iterator.jump
        jumped_node_new = move_to_nth_node(original_new_head, jumped_node.data)
        iterator_copy.jump = jumped_node_new
        original_new_head = new_head
        iterator = iterator.next
        iterator_copy = iterator_copy.next

    return save_the_head


def deserialize_orig_list(head, new_head):
    save_the_head = head
    while head is not None:
        head.data = new_head.data
        head = head.next
        new_head = new_head.next
    return save_the_head


def create_list(size, data):
    count = 0
    head = LinkedListNode(data[count])
    save_the_head = head
    count += 1
    while count < size:
        new_node = LinkedListNode(data[count])
        head.next = new_node
        head = new_node
        count += 1
    return save_the_head


def create_jumps(head, data):
    original_head = head
    save_the_head = head
    for index, node_number in enumerate(data):
        jump_to = move_to_nth_node(original_head, node_number)
        head.jump = jump_to
        head = head.next
        original_head = save_the_head
    return save_the_head


if __name__ == "__main__":
    head = create_list(5, ['a', 'b', 'c', 'd', 'e'])
    head = create_jumps(head, [3, 1, 1, 3, 2])
    new_head = copy_basic_list(head)
    head = serialize_orig_list(head)
    new_head = copy_jumps(head, new_head)
    head = deserialize_orig_list(head, new_head)
    print(2)



