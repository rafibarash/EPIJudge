from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    if not square_matrix:
        return []

    def true_len(M):
        i = 0
        for row in M:
            for col in M:
                i += 1
        return i

    ans = set()
    row, col, = 0, 0
    trav_col, going_right_or_down = True, True
    true_len = true_len(square_matrix)
    while len(ans) < true_len:
        if trav_col:
            # two cases
            if col >= len(square_matrix[row]) or col < 0 or square_matrix[row][col] in ans:
                trav_col = not trav_col
                col = col - 1 if going_right_or_down else col + 1
                row = row + 1 if going_right_or_down else row - 1
            else:
                ans.add(square_matrix[row][col])
                col = col + 1 if going_right_or_down else col - 1
        else:
            # also two cases
            if row >= len(square_matrix) or row < 0 or square_matrix[row][col] in ans:
                trav_col, going_right_or_down = not trav_col, not going_right_or_down
                row = row - 1 if going_right_or_down else row + 1
                col = col - 1 if going_right_or_down else col + 1
            else:
                ans.add(square_matrix[row][col])
                row = row + 1 if going_right_or_down else row - 1
    return list(ans)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
