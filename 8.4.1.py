class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.jump = None
        self.next = next

    def __str__(self):
        return str(self.data)


def create_copy_appended(head):
    save_the_head = head

    while head is not None:
        new_node = LinkedListNode(head.data)
        heads_next = head.next
        head.next = new_node
        new_node.next = heads_next
        head = heads_next
    return save_the_head


def create_chains(head):
    save_the_head = head

    while head is not None:
        heads_jump_to = head.jump
        new_list_object = head.next
        new_list_object.jump = heads_jump_to.next
        head = new_list_object.next

    return save_the_head


def separate_lists(head):
    new_head = head.next
    save_the_new_head = new_head
    save_the_old_head = head

    while head is not None:
        head.next = new_head.next
        if head.next is None:
            break
        else:
            head = head.next
            new_head.next = head.next
            new_head = new_head.next

    return save_the_old_head, save_the_new_head


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


def move_to_nth_node(head, node_number):
    count = 1
    while count < node_number:
        count += 1
        head = head.next
    return head


if __name__ == "__main__":
    head = create_list(5, ['a', 'b', 'c', 'd', 'e'])
    head = create_jumps(head, [3, 1, 1, 3, 2])
    appended_head = create_copy_appended(head)
    appended_head = create_chains(appended_head)
    head, new_head = separate_lists(appended_head)
    print(2)