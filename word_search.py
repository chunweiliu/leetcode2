"""DFS backtracking every 3 possible directions to find the word

Time: O(mn 3^k), where k is the length of the word
Space: O(4mn) for the recursive call
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def search(word, row, col, visited):
            if not word:
                return True
                
            if 0 <= row < m and 0 <= col < n and not visited[row][col] and board[row][col] == word[0]:        
                # Backtracking
                found = False                
                visited[row][col] = True
                          
                for nr, nc in (row-1, col), (row+1, col), (row, col-1), (row, col+1):
                    found |= search(word[1:], nr, nc, visited)
                    
                    # Early break without trying unnecessary loop
                    if found:
                        break
                
                visited[row][col] = False                    
                return found
            return False
        
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        
        for row in range(m):
            for col in range(n):
                if search(word, row, col, visited):
                    return True                
        return False