"""Given previous transactions, find a minimum step for balancing the transactions.

    Input:
    [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

    Output:
    1

    Explanation:
    Person #0 gave person #1 $10.
    Person #1 gave person #0 $1.
    Person #1 gave person #2 $5.
    Person #2 gave person #0 $5.

    Therefore, person #1 only need to give person #0 $4, and all debt is settled.

    * Graph? Might not need
    * Count the number of positives and negatives, pick the larger
        [[0,1,5],[2,3,1],[2,0,1],[4,0,2]]

       -2     +5     -2     +1     -2
        0      1      2      3      4
    *

Time: O(n)
Space: O(n)
"""
from collections import defaultdict


class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        person = defaultdict(int)

        for sender, receiver, money in transactions:
            person[sender] -= money
            person[receiver] += money

        negatives = sum(1 for money in person.values() if money < 0)
        positives = sum(1 for money in person.values() if money > 0)
        return max(positives, negatives)

        