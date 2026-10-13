def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)


def check_winner(b):
    # Check rows, columns, and diagonals
    lines = (
        b +  # 3 rows
        [[b[r][c] for r in range(3)] for c in range(3)] +  # 3 columns
        [[b[0][0], b[1][1], b[2][2]], [b[0][2], b[1][1], b[2][0]]]  # 2 diagonals
    )
    for line in lines:
        if line[0] == line[1] == line[2] != " ":
            return line[0]
    return None


def play_game():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    for move in range(9):
        print_board(board)
        while True:
            try:
                r = int(input(f"Player {player}, enter row (0-2): "))
                c = int(input(f"Player {player}, enter col (0-2): "))
                if 0 <= r < 3 and 0 <= c < 3 and board[r][c] == " ":
                    board[r][c] = player
                    break
                print("Invalid move. Cell occupied or out of bounds.")
            except ValueError:
                print("Please enter valid integers (0-2).")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return

        player = "O" if player == "X" else "X"

    print_board(board)
    print("It's a draw!")


play_game()
