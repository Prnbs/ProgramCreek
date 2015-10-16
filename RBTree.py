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

    def restructure(self, curr_node, direction_of_incoming):
        print "-->",curr_node
        print "---->",curr_node.children[direction_of_incoming]
        # left rotate if direction of incoming = 1
        if direction_of_incoming:
            self.rotate(curr_node, direction_of_incoming)
        # right rotation
        else:
            self.rotate(curr_node, direction_of_incoming)

    def rotate_left(self, curr_node):
        parent = curr_node.parent
        grandparent = parent.parent
        grandparent.children[0] = curr_node
        curr_node.self_location = False
        parent.parent = curr_node
        parent.children[1] = curr_node.children[0]
        curr_node.children[0].self_location = True
        curr_node.children[0] = parent
        curr_node.parent = grandparent
        return parent, curr_node

    def rotate_right(self, curr_node):
        parent = curr_node.parent
        # root!!
        if parent.parent is not None:
            grandparent = parent.parent
            grandparent.children[1] = curr_node
            curr_node.parent = grandparent
            curr_node.self_location = True
        else:
            curr_node.self_location = -1
            self.root = curr_node
            parent.self_location = True
        parent.parent = curr_node
        parent.children[0] = curr_node.children[1]
        curr_node.children[1].self_location = False
        curr_node.children[1] = parent

        return parent, curr_node


    def rotate(self, curr_node, direction):
        curr_node.parent.children[direction] = curr_node.children[not direction]
        curr_node.children[not direction] = curr_node.parent
        # check for root
        if curr_node.parent.parent is not None:
            curr_node.parent.parent.children[direction] = curr_node
            curr_node.colour = "B"
        else:
            # For root
            self.root = curr_node
            self.root.colour = "B"

    def insert(self, item, curr_node):
        inserted_at, direction = self.insert_as_bst(item, curr_node)
        if direction is -1:
            return
        while inserted_at.self_location is not -1 and inserted_at.colour is "R":
            print "Parent:", inserted_at
            print "     Node:",  inserted_at.children[direction]
            # inserted_at is the parent of node just inserted
            if inserted_at.parent.colour is "R":
                parent = inserted_at.parent
                sibling = parent.children[not direction]
                uncle = parent.parent.children[not parent.self_location]

                if parent.colour is "R" and uncle is None or uncle.colour is "R":
                    # push blackness down from grandparent
                    uncle.colour = uncle.parent.colour
                    parent.colour = uncle.parent.colour
                    uncle.parent.colour = "R"

                inserted_at = uncle.parent
                node = None
                node_parent = None
                if inserted_at.parent is not None and (inserted_at.colour is "R" and inserted_at.parent.colour is "R"):
                    # change inserted_at to parent
                    node, node_parent = self.rotate_left(inserted_at)
                if node is not None and node.colour is "R" and node_parent.colour is "R":
                    if node.self_location is False and node_parent.self_location is False:
                        # right rotate
                        self.rotate_right(node_parent)
                    # elif node.self_location is True and node_parent.self_location is True:
                    #     self.rotate_left(inserted_at)
                else:
                    break
            else:
                break
        self.root.colour = "B"


if __name__ == '__main__':
    rbTree = RBTree()
    rbTree.insert(11, rbTree.root)
    rbTree.insert(2, rbTree.root)
    rbTree.insert(14, rbTree.root)
    rbTree.insert(15, rbTree.root)
    rbTree.insert(1, rbTree.root)
    rbTree.insert(7, rbTree.root)
    rbTree.insert(5, rbTree.root)
    rbTree.insert(8, rbTree.root)
    rbTree.insert(4, rbTree.root)
    # rbTree.insert(20, rbTree.root)
    print "end"




