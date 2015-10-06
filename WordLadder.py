__author__ = 'psinha4'

class Node:
    def __init__(self, _word):
        self.word = _word
        self.l_adjacents = []
        self.visited = False


class WordLadder:
    def __init__(self, _dict):
        self.dict = _dict
        self.graph = []
        self.queue = []
        for i, elem in enumerate(self.dict):
            node = Node(elem)
            self.graph.append(node)

        for i in range(len(self.dict)-1):
            for j in range(len(self.dict)):
                if i == j:
                    continue
                if self.distance(self.graph[i].word, self.graph[j].word, 0) == 1:
                    self.graph[i].l_adjacents.append(self.graph[j])

    def distance(self, left, right, i_currcost):
        if len(left) != len(right):
            return 100
        if len(left) == 0:
            return i_currcost
        else:
            if left[0] == right[0]:
                return self.distance(left[1:], right[1:], i_currcost)
            else:
                return self.distance(left[1:], right[1:], i_currcost+1)

    def bfs_init(self, start_idx, end_idx):
        i_distance = 0
        end_word = self.dict[end_idx]
        queue = []
        queue.extend(self.graph[start_idx].l_adjacents)
        while len(queue) != 0:
            i_distance += 1
            queue = self.bfs(queue, end_word)
        print i_distance

    def bfs(self, queue, end_word):
        new_queue = []
        for i, nodes in enumerate(queue):
            if nodes.visited:
                continue
            nodes.visited = True
            if nodes.word == end_word:
                return new_queue
            new_queue.extend(nodes.l_adjacents)
        return new_queue


if __name__ == '__main__':
    start = "dog"
    end = "him"
    dict = ["dam","dat", "ham", "dag"]
    dict.insert(0, start)
    dict.append(end)
    ladder = WordLadder(dict)
    ladder.bfs_init(0, len(dict)-1)

