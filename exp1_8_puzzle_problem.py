from collections import deque


def solve_8_puzzle(board):
    # Flatten 2D board to 1D tuple (0 represents the blank space)
    start = tuple(tile for row in board for tile in row)
    goal = (0, 1, 2, 3, 4, 5, 6, 7, 8)

    # Adjacency map for valid blank tile movements in 3x3 grid
    moves = {
        0: (1, 3), 1: (0, 2, 4), 2: (1, 5),
        3: (0, 4, 6), 4: (1, 3, 5, 7), 5: (2, 4, 8),
        6: (3, 7), 7: (4, 6, 8), 8: (5, 7)
    }

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        state, depth = queue.popleft()
        if state == goal:
            return depth

        z = state.index(0)
        for swap in moves[z]:
            nxt = list(state)
            nxt[z], nxt[swap] = nxt[swap], nxt[z]
            nxt = tuple(nxt)
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, depth + 1))
    return -1


matrix = [
    [3, 1, 2],
    [4, 7, 5],
    [6, 8, 0]
]

print(solve_8_puzzle(matrix))
