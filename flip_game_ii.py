"""Find if we have an optimal stratge for player 1 to win the flip game.
   Each round, a player can turn '++' to '--'. The person executes the last round win.

    ++++
    +--+ <- first player's move
    => True

    You win only when you can make the last move.
    So '++' must be in current state but not in the next state

Time: O(2^m)
Space: O(1)
"""

class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memo = {}
        
        def win(s):
            if s not in memo:                                    
                memo[s] = any(s[i:i+2] == '++' and not win(s[:i] + '-' + s[i+2]:)
                              for i in range(len(s)))
            return memo[s]

        return win(s)
        