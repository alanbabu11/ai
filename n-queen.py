n = int(input())
boards = []
cols = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)

def dfs(i,board):
  if i == n:
    boards.append(board)
    return

  for col in range(n):
    if cols[col] or diag1[i + col] or diag2[col - i + n - 1]:
      continue
    cols[col] = diag1[i + col] = diag2[col - i + n - 1] = True
    dfs(i + 1, board + ['.' * col + 'Q' + '.' * (n - col - 1)])
    cols[col] = diag1[i + col] = diag2[col - i + n - 1] = False

dfs(0, [])
return boards
