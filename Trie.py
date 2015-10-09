__author__ = 'psinha4'

class TrieNode:
    def __init__(self, letter):
        self.alphabet = letter
        self.leaf = False
        self.children = [None] * 26

    def __str__(self):
        return self.alphabet

    __repr__ = __str__


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def add_word(self, word):
        curr_node = self.root
        for character in word:
            index = ord(character) - ord("a")
            if curr_node.children[index] is None:
                new_node = TrieNode(character)
                curr_node.children[index] = new_node
                curr_node = new_node
            else:
                curr_node = curr_node.children[index]
        curr_node.leaf = True

if __name__ == '__main__':
    trie = Trie()
    trie.add_word("word")
    print trie.root.children
