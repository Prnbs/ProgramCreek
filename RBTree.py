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

    __repr__ = __str__


class RBTree:
    def __init__(self):
        self.root = None

    def insert_as_bst(self, item, curr_node):
        inserted = False
        direction = 0
        if curr_node is not None:
            direction = (curr_node.data < item)
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

    def rotate(self, curr_node, left=True):
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
                grand_parent.children[left] = parent.children[not left]
                if parent.children[not left] is not None:
                    parent.children[not left].parent = grand_parent
                parent.children[not left] = grand_parent
                grand_parent.parent = parent
                grand_parent.self_location = not left
                # swap colours
                parent.colour, grand_parent.colour = grand_parent.colour, parent.colour
                return parent
            else:
                # Not in line
                grand_parent.children[curr_node.parent.self_location] = curr_node
                curr_node.self_location = parent.self_location
                curr_node.parent = grand_parent
                if curr_node.children[not left] is not None:
                    curr_node.children[not left].parent = parent
                    parent.children[not left].self_location = not parent.children[left].self_location
                parent.children[left] = curr_node.children[not left]
                curr_node.children[not left] = parent
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
                            inserted_at = self.rotate(inserted_at, left=False)
                        else:
                            inserted_at = self.rotate(inserted_at, left=True)
                        continue
                    else:
                        # parent is right child, inserted_at is left child
                        if not parent.self_location:
                            inserted_at = self.rotate(inserted_at, left=True)
                        else:
                            inserted_at = self.rotate(inserted_at, left=False)
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
    list_of_items = [50, 1, 2, 3, 4, -4, 10, 5, 6, 7, 8, 9]

    for data in list_of_items:
        rbTree.insert(data, rbTree.root)
        print data

    print "end"




