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
        if parent.parent is not None:
            grand_parent = parent.parent
            if grand_parent.self_location is -1 and grand_parent.self_location == parent.self_location\
                    and parent.self_location == curr_node.self_location:
                parent.self_location = -1
                self.root = parent
            # swap colous
            parent.colour, grand_parent.colour = grand_parent.colour, parent.colour
            grand_parent.children[1] = parent.children[0]
            parent.children[0] = grand_parent
            # now invert self_locations of the above
            if grand_parent.children[1] is not None:
                grand_parent.children[1].self_location = not grand_parent.children[1].self_location
            if parent.children[0] is not None:
                parent.children[0].self_location = not parent.children[0].self_location

            parent.self_location, grand_parent.self_location = grand_parent.self_location, parent.self_location


        return parent, curr_node


    def rotate_right(self, curr_node):
        parent = curr_node.parent
        if parent.parent is not None:
            grand_parent = parent.parent
            if grand_parent.self_location is -1:
                parent.self_location = -1
                self.root = parent
            # swap colours
            parent.colour, grand_parent.colour = grand_parent.colour, parent.colour
            grand_parent.children[0] = parent.children[1]
            parent.children[1] = grand_parent
            # now invert self_locations of the above
            if grand_parent.children[0] is not None:
                grand_parent.children[0].self_location = not grand_parent.children[0].self_location
            if parent.children[1] is not None:
                parent.children[1].self_location = not parent.children[1].self_location

            parent.self_location, grand_parent.self_location = grand_parent.self_location, parent.self_location


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

                # uncle rule takes precedence
                if parent.colour is "R" and uncle is not None and uncle.colour is "R":
                    # push blackness down from grandparent
                    if uncle is not None:
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
                            inserted_at, somm = self.rotate_right(inserted_at)
                        else:
                            inserted_at, somm = self.rotate_left(inserted_at)
                        continue
                    else:
                        # parent is right child, inserted_at is left child
                        if not parent.self_location:
                            inserted_at, somm = self.rotate_left(inserted_at)
                        else:
                            inserted_at, somm = self.rotate_right(inserted_at)
                        continue


                inserted_at = parent.parent
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
    # rbTree.insert(10, rbTree.root)
    # rbTree.insert(20, rbTree.root)
    # rbTree.insert(30, rbTree.root)


    print "end"




