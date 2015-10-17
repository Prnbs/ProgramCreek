__author__ = 'psinha4'

class RBNode:
    def __init__(self, data, colour, parent=None, direction=-1):
        self.data = data
        self.parent = parent
        self.children = [None, None]
        self.colour = colour
        # index to self.children
        # -1 for root, 0 for left, 1 for right
        self.self_location = direction

    def __str__(self):
        return str(self.data) + self.colour

    # # will assign thisNode's location to old root
    # def set_as_root(self, thisNode):
    #     self.root.self_location = thisNode.self_location
    #     self.root


    __repr__ = __str__


class RBTree:
    def __init__(self):
        self.root = None

    def insert_as_bst(self, item, curr_node):
        inserted = False
        direction = 0
        if curr_node is not None:
            direction = (curr_node.data <= item)
            if curr_node.children[direction] is None:
                curr_node.children[direction] = RBNode(item, "R", parent=curr_node, direction=direction)
                inserted = True
            else:
                return self.insert_as_bst(item, curr_node.children[direction])
        else:
            # root is empty
            self.root = RBNode(item, "B")
            return self.root, -1
        # now recolour or restructure
        if inserted:
            return curr_node.children[direction], direction

    def rotate_left(self, curr_node):
        left = False
        right = True
        parent = curr_node.parent
        if parent.parent is not None:
            grand_parent = parent.parent

            if grand_parent.children[right] is not None and \
                                grand_parent.children[right] == parent and \
                                parent.self_location == curr_node.self_location:
                # all in a line
                if grand_parent.self_location is -1:
                    # grand parent is root
                    self.root = parent
                    parent.self_location = -1
                else:
                    # not root, but they are in line
                    if grand_parent.parent is not None:
                        grand_parent.parent.children[grand_parent.self_location] = parent
                parent.parent = grand_parent.parent
                grand_parent.children[right] = parent.children[left]
                if parent.children[left] is not None:
                    parent.children[left].parent = grand_parent
                parent.children[left] = grand_parent
                grand_parent.parent = parent
                grand_parent.self_location = left
                # swap colours
                parent.colour, grand_parent.colour = grand_parent.colour, parent.colour
                return parent
            else:
                # Not in line
                # first swap parent and curr_node
                parent.children[right] = curr_node.children[left]
                if curr_node.children[left] is not None:
                    curr_node.children[left].parent = parent
                    curr_node.children[left].self_location = not curr_node.children[left].self_location
                # now swap curr node and parent
                grand_parent.children[parent.self_location] = curr_node
                curr_node.self_location = parent.self_location
                curr_node.parent = grand_parent

                curr_node.children[left] = parent
                parent.parent = curr_node
                return parent

    def rotate_right(self, curr_node):
        left = False
        right = True
        parent = curr_node.parent
        if parent.parent is not None:
            grand_parent = parent.parent

            if grand_parent.children[left] is not None and \
                                grand_parent.children[left] == parent and \
                                parent.self_location == curr_node.self_location:
                # all in a line
                if grand_parent.self_location is -1:
                    # grand parent is root
                    self.root = parent
                    parent.self_location = -1
                else:
                    # not root, but they are in line
                    if grand_parent.parent is not None:
                        grand_parent.parent.children[grand_parent.self_location] = parent
                parent.parent = grand_parent.parent
                grand_parent.children[left] = parent.children[right]
                if parent.children[right] is not None:
                    parent.children[right].parent = grand_parent
                parent.children[right] = grand_parent
                grand_parent.parent = parent
                grand_parent.self_location = right
                # swap colours
                parent.colour, grand_parent.colour = grand_parent.colour, parent.colour
                return parent
            else:
                # Not in line
                # first swap parent and curr_node
                parent.children[right] = curr_node.children[left]
                if curr_node.children[left] is not None:
                    curr_node.children[left].parent = parent
                    curr_node.children[left].self_location = not curr_node.children[left].self_location
                # now swap curr node and parent
                grand_parent.children[parent.self_location] = curr_node
                curr_node.self_location = parent.self_location
                curr_node.parent = grand_parent

                curr_node.children[left] = parent
                parent.parent = curr_node
                return parent

    def insert(self, item, curr_node):
        inserted_at, direction = self.insert_as_bst(item, curr_node)
        if direction is -1:
            return
        while inserted_at is not None and inserted_at.self_location is not -1 and inserted_at.colour is "R":
            print "Parent:", inserted_at
            print "     Node:",  inserted_at.children[direction]
            # inserted_at is the parent of node just inserted
            if inserted_at.parent is not None and inserted_at.parent.colour is "R":
                parent = inserted_at.parent
                sibling = parent.children[not direction]
                uncle = parent.parent.children[not parent.self_location]

                # uncle rule takes precedence
                if parent.colour is "R" and uncle is not None and uncle.colour is "R":
                    # push blackness down from grandparent
                    if uncle is not None and uncle.parent is not None:
                        uncle.colour = uncle.parent.colour
                    parent.colour = parent.parent.colour
                    parent.parent.colour = "R"
                    inserted_at = parent.parent
                    continue

                # check if new node and parent (if both red) are all left most or right most entities
                if parent.colour is "R":
                    if parent.self_location == inserted_at.self_location:
                        # if left most
                        if not parent.self_location:
                            inserted_at = self.rotate_right(inserted_at)
                        else:
                            inserted_at = self.rotate_left(inserted_at)
                        continue
                    else:
                        # parent is right child, inserted_at is left child
                        if not parent.self_location:
                            inserted_at = self.rotate_left(inserted_at)
                        else:
                            inserted_at = self.rotate_right(inserted_at)
                        continue
            else:
                break
        self.root.colour = "B"


if __name__ == '__main__':
    rbTree = RBTree()
    # rbTree.insert(10, rbTree.root)
    # rbTree.insert(30, rbTree.root)
    # rbTree.insert(40, rbTree.root)
    # rbTree.insert(50, rbTree.root)
    # rbTree.insert(60, rbTree.root)
    # rbTree.insert(80, rbTree.root)
    # rbTree.insert(90, rbTree.root)
    # rbTree.insert(100, rbTree.root)


    # rbTree.insert(100, rbTree.root)
    # rbTree.insert(90, rbTree.root)
    # rbTree.insert(80, rbTree.root)
    # rbTree.insert(70, rbTree.root)
    # rbTree.insert(60, rbTree.root)
    # rbTree.insert(50, rbTree.root)
    # rbTree.insert(40, rbTree.root)
    # rbTree.insert(30, rbTree.root)
    # rbTree.insert(10, rbTree.root)
    list_of_items = [50, 10, 20, 5, 3, -4, 10, 5, 6, 7, 8, 9, 34, 76, 58, 92, -12, -19, 1000,700, 900,800]

    for data in list_of_items:
        rbTree.insert(data, rbTree.root)
        print data

    print "end"




