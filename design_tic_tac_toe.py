"""Use arrays for counting 'x' and 'o' for each rows, columns and diagnal.

Time: O(1)
Space: O(n)
"""

class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.digs = [0, 0]

        self.game = 0
        
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        n = self.n
        if not self.game and 0 <= row < n and 0 <= col < n:
            count = 1 if player == 1 else -1

            self.rows[row] += count
            self.cols[col] += count
            if row == col:
                self.digs[0] += count
            if row + col == n - 1:
                self.digs[1] += count

            if n in map(abs, [self.rows[row], self.cols[col], self.digs[0], self.digs[1]]):
                self.game = player

        return self.game


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)