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

    def find_all_words(self, prefix, curr_node, l_words_found, str_partial_word):
        # if prefix is empty now loop through all the children
        if len(prefix) == 0:
            for node in curr_node.children:
                if node is not None:
                    # the partial words till here will diverge because of the loop above
                    str_partial_word_for_this_path = str_partial_word + node.alphabet
                    curr_node = node
                    if node.leaf:
                        l_words_found.append(str_partial_word_for_this_path)
                    self.find_all_words(prefix, curr_node, l_words_found, str_partial_word_for_this_path)
            return l_words_found
        index = ord(prefix[0]) - ord("a")
        # if head of prefix is not found
        if curr_node.children[index] is None:
            return l_words_found
        # store the partial word found till now
        str_partial_word += curr_node.children[index].alphabet
        curr_node = curr_node.children[index]
        # if the full prefix itself contains a valid word
        if curr_node.leaf and len(prefix) <= 1:
            l_words_found.append(str_partial_word)
        return self.find_all_words(prefix[1:], curr_node, l_words_found, str_partial_word)


if __name__ == '__main__':
    trie = Trie()
    lines = [line.rstrip('\n') for line in open('wordsEn.txt')]
    for word in lines:
        trie.add_word(word)
    str_prefix = "blacksm"
    l_all_words = trie.find_all_words(str_prefix, trie.root, [], "")
    print (l_all_words)
