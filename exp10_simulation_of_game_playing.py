def print_board(b):
    for row in b:
        print(row)


def check_winner(b):
    # Check all rows, columns, and diagonals for 3 matching tokens
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != 0:
            return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != 0:
            return b[0][i]
    if b[0][0] == b[1][1] == b[2][2] != 0:
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != 0:
        return b[0][2]
    return 0


board = [[0]*3 for _ in range(3)]
player = 1

while True:
    print_board(board)
    try:
        r = int(input(f"Player {player}, enter row (0-2): "))
        c = int(input(f"Player {player}, enter col (0-2): "))
        if 0 <= r < 3 and 0 <= c < 3 and board[r][c] == 0:
            board[r][c] = player
        else:
            print("Invalid move. Try again.")
            continue
    except ValueError:
        print("Enter valid integers (0-2).")
        continue

    winner = check_winner(board)
    if winner:
        print_board(board)
        print(f"Player {winner} wins!")
        break

    if all(cell != 0 for row in board for cell in row):
        print_board(board)
        print("It's a draw!")
        break

    player = 3 - player  # Toggle between 1 and 2
