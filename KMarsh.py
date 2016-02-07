def create_marsh(n, m, obstacles):
    marsh_vert = [[0 for x in range(m)] for x in range(n)]
    marsh_hori = [[0 for x in range(m)] for x in range(n)]

    for i in range(n):
        for j in range(m):
            if obstacles[i][j] is False:
                if j > 0:
                    marsh_hori[i][j] = marsh_hori[i][j-1] + 1
                if i > 0:
                    marsh_vert[i][j] = marsh_vert[i-1][j] + 1
            else:
                marsh_vert[i][j] = -1
                marsh_hori[i][j] = -1

    return marsh_hori, marsh_vert


def calculate_perimeter(n, m, marsh_vert, marsh_hori, obstacles):
    max_perimeter = 0
    for start_i in range(n-1, 0, -1):
        for start_j in range(m-1, 0, -1):
            if obstacles[start_i][start_j] is True:
                continue
            up_stride = marsh_vert[start_i][start_j]
            left_stride = marsh_hori[start_i][start_j]

            if up_stride == 0 or left_stride == 0:
                continue

            top_left_i = start_i - up_stride
            top_left_j = start_j - left_stride

            # keep up_stride constant and check all left strides
            for j in range(top_left_j, start_j):
                if obstacles[top_left_i][j] is True:
                    continue
                down_sweep = marsh_vert[start_i][j]
                if down_sweep >= marsh_vert[start_i][start_j]:
                    # once down sweep works check for left sweep
                    left_sweep = marsh_hori[top_left_i][start_j] - marsh_hori[top_left_i][j]
                    if left_sweep >= (start_j - j):
                        # max rect in left sweep found
                        l = start_j - j
                        b = min(down_sweep, marsh_vert[start_i][start_j])
                        perimeter = 2 * (l + b)
                        max_perimeter = max(max_perimeter, perimeter)
                        break

            # keep left_stride consatnt and check all up strides
            for i in range(top_left_i, start_i):
                if obstacles[i][top_left_j] is True:
                    continue
                down_sweep = marsh_vert[start_i][top_left_j]
                if down_sweep >= start_i - i:
                    # once down sweep works check for left sweep
                    left_sweep = marsh_hori[i][start_j]
                    if left_sweep >= start_j - top_left_j:
                        # max rect in left sweep found
                        l = start_j - top_left_j
                        b = start_i - i
                        perimeter = 2 * (l + b)
                        max_perimeter = max(max_perimeter, perimeter)
                        break

    return max_perimeter


if __name__ == '__main__':
    [n, m] = [int(x) for x in input().split()]
    obstacles = [[] for x in range(n)]
    for i in range(n):
       line = str(input())
       obstacles[i].extend([True if x == 'x' else False for x in line])

    hori, vert = create_marsh(n, m,obstacles)

    max_perimeter = calculate_perimeter(n, m, vert, hori, obstacles)
    if max_perimeter == 0:
        print("impossible")
    else:
        print (max_perimeter)
