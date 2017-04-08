"""Find the next state of the board, follow by the rules:

    - Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    - Any live cell with two or three live neighbors lives on to the next generation.
    - Any live cell with more than three live neighbors dies, as if by over-population.
    - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

    Follow up:
        - Inplace
        => Use 2 bits for different previous and current states
           00
           ^  current
            ^ previous 

    * Avoid naming (i, j) within the for loop
    * Avoid short global variables
        - n has been used in elsewhere
    * board = G won't change the memory of the board pointed to.
      It just points the label 'board' to the memoery G.

Time: O(mn)
Space: O(1)
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def neighbor(r, c):
            rows = [max(0, r - 1), min(r + 2, m)]
            cols = [max(0, c - 1), min(c + 2, n)]

            count = 0
            for i in range(*rows):
                for j in range(*cols):
                    if i == r and j == c:
                        continue
                    count += board[i][j] & 1
            return count

        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                neighbor_lives = neighbor(i, j)
                # Current live
                if board[i][j] & 1:
                    if 2 <= neighbor_lives <= 3:
                        board[i][j] += 2
                    
                # Current not live
                else:
                    if neighbor_lives == 3:
                        board[i][j] += 2
                    
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                board[i][j] >>= 1

# board = [[1,1],
#          [1,0]]
# board = [[0,0,0,0],
#          [0,1,1,0],
#          [0,1,1,0],
#          [0,0,0,0]]
# Solution().gameOfLife(board)