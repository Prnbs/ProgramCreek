__author__ = 'prnbs'


class Link:
    def __init__(self, data):
        self.next = None
        self.data = data


def insert(head, data):
    while head.next is not None:
        head = head.next
    # last node found
    new_node = Link(data)
    head.next = new_node


def delete(head, data):
    prev_node = head
    while head.next is not None:
        if head.data == data:
            prev_node.next = head.next
        prev_node = head
        head = head.next


def reverse(curr_node):
    look_ahead = curr_node.next
    curr_node.next = None
    while look_ahead is not None:
        next_node = look_ahead.next
        look_ahead.next = curr_node
        curr_node = look_ahead
        look_ahead = next_node
    # reached the end
    return curr_node


def length(head):
    length = 0
    while head is not None:
        head = head.next
        length += 1
    return length


# generic merge for two lists which may have unequal length
def merge(head_one, head_two):
    merged_head = head_one
    head_one_next = head_one.next
    head_two_next = head_two.next

    while head_one_next is not None and head_two_next is not None:
        head_one.next = head_two
        head_two.next = head_one_next

        head_one = head_one_next
        head_two = head_two_next

        if head_one_next.next is not None:
            head_one_next = head_one_next.next
        else:
            head_one_next = None
        if head_two_next.next is not None:
            head_two_next = head_two_next.next
        else:
            head_two_next = None

    # we still need to update the last item in list 2
    head_one.next = head_two
    head_one = head_one.next

    if head_one_next is not None:
        head_one.next = head_one_next
    elif head_two_next is not None:
        head_one.next = head_two_next

    return merged_head


def show_list(head):
    while head is not None:
        print (head.data)
        head = head.next


def zip(head):
    size = length(head)
    curr_head = head
    prev_node = curr_head
    count = 0
    while count < size/2:
        prev_node = curr_head
        curr_head = curr_head.next
        count += 1
    new_head = curr_head
    prev_node.next = None

    new_head = reverse(new_head)
    return merge(head, new_head)

if __name__ == '__main__':
    head = Link(1)
    insert(head, 2)
    insert(head, 3)
    insert(head, 4)
    insert(head, 5)
    insert(head, 6)
    insert(head, 7)
    insert(head, 8)
    insert(head, 9)
    insert(head, 10)

    head_two = Link(100)
    insert(head_two, 120)
    insert(head_two, 130)

    merged_list = merge(head_two, head)
    print(show_list(merged_list))
