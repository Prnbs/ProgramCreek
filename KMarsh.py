class KMarch:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.Matrix = []
        self.perimeter = [[0 for x in range(M)] for y in range(N)]

    def create_marsh(self):
        # set x, y as initial points
        for X in range(self.M):
            for Y in range(self.N):
                # initialize row X
                self.perimeter[X][Y] = 0
                for x in range(X+1, self.M):
                    if self.Matrix[Y][x] == '.':
                        self.perimeter[Y][x] = self.perimeter[Y][x-1] + 1
                    else:
                        self.perimeter[Y][x] = -1
                # initialize column Y
                for y in range(Y+1, self.N):
                    if self.Matrix[y][X] == '.':
                        self.perimeter[y][X] = self.perimeter[y-1][X] + 1
                    else:
                        self.perimeter[y][X] = -1
                # set other end of rectangle
                for y in range(Y+1, self.N):
                    for x in range(X+1, self.M):
                        if self.Matrix[x-1][y] == '.' and self.Matrix[x][y-1] == '.':
                            # special case of 1
                            if self.perimeter[x-1][y] == 1 and self.perimeter[x][y-1] == 1:
                                self.perimeter[x][y] = 4
                            elif self.perimeter[x-1][y] != -1 and self.perimeter[x][y-1] != -1:
                                self.perimeter[x][y] = 2 + max(self.perimeter[x-1][y], self.perimeter[x][y-1])
                            else:
                                self.perimeter[x][y] = -1
                        else:
                            self.perimeter[x][y] = -1


if __name__ == '__main__':
    [N, M] = map(int, input().strip().split())
    marsh = KMarch(N, M)
    for i in range(N):
        marsh.Matrix.extend(input().strip().split())
    marsh.create_marsh()
    print(marsh.perimeter)