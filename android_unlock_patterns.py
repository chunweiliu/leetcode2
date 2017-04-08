"""Return the number of Android unlock pattern for a 3 x 3 board,
   with consist of minimum of m keys and maximum n keys (1 <= m <= n <= 9)

    | 1 | 2 | 3 |
    | 4 | 5 | 6 |
    | 7 | 8 | 9 |

    m = 1, n = 1
    => 9

    Pick 5, 8! le


    Count path by DFS, the question is what's the next state can be.

    * Jump table

Time: O(c^n)
Space: O(1), since the board size is fix
"""

class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        jump = {}
        jump[(1, 3)] = jump[(3, 1)] = 2
        jump[(1, 7)] = jump[(7, 1)] = 4
        jump[(3, 9)] = jump[(9, 3)] = 6
        jump[(7, 9)] = jump[(9, 7)] = 8
        for i in range(1, 10):
            if i == 5:
                continue
            jump[(i, 10 - i)] = 5

        def DFS(current, seen, remain):
            if remain == 0:
                return 1

            count = 0
            seen.add(current)
            
            for next in range(1, 10):
                if (next not in seen and 
                    ((current, next) not in jump or 
                     jump[(current, next)] in seen)):
                    count += DFS(next, seen, remain - 1)

            seen.remove(current)
            return count
        
        count = 0
        seen = set()
        for i in range(m, n + 1):       
            count += DFS(1, seen, i - 1) * 4  # 1, 3, 7, 9
            count += DFS(2, seen, i - 1) * 4  # 2, 4, 6, 8
            count += DFS(5, seen, i - 1)
        return count
