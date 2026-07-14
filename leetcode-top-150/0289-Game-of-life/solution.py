class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None
        """
        m = len(board)
        n = len(board[0])

        directions = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1),          (0,1),
            (1,-1),  (1,0),  (1,1)
        ]

        # First pass: mark transitions
        for i in range(m):
            for j in range(n):

                live = 0

                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy

                    if 0 <= ni < m and 0 <= nj < n:
                        if board[ni][nj] == 1 or board[ni][nj] == -1:
                            live += 1

                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = -1
                else:
                    if live == 3:
                        board[i][j] = 2

        # Second pass: finalize states
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1