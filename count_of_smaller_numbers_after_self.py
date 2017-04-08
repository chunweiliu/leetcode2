"""Count of smaller number after self **Inverse Count**

    Given nums = [5, 2, 6, 1]

    To the right of 5 there are 2 smaller elements (2 and 1).
    To the right of 2 there is only 1 smaller element (1).
    To the right of 6 there is 1 smaller element (1).
    To the right of 1 there is 0 smaller element.

    => [2, 1, 1, 0]

    - Binary Search Tree
        * Implement RB Tree is not practical
        * If it is an unbalance BST, the insert and query time ~ O(n)

        [3, 2, 2, 6, 1]

        Insert node backward, Sum up (left, count) tuple if we trun right 
        to count the smaller number after self. For example, if insert (5),
        the answer would be 4

                1(0, 1)
                     \
                     6(3, 1)
                     /
                   2(0, 2)
                       \
                        3(0, 1)
                         \
                          5 => (0, 1) + (0, 2) + (0, 1) = 4

        Time: O(n logn) in a RB Tree; O(n^2) for unbalance tree

    - Merge Sort

        The smaller numbers on the right of a number are exactly those that 
        jump from its right to its left during a stable sort.

        Why merge sort? Why not quick sort?

        => Merge sort give you partial order

        http://www.geeksforgeeks.org/counting-inversions/


Time: O(n log n)
Space: O(n)
"""
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(enum):
            half = len(enum) / 2
            if half:
                # Divide
                left, right = sort(enum[:half]), sort(enum[half:])

                # Merge (insert) backward
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        # The original index add *all* the smaller number
                        # This is why we want merge sort, because you can
                        # add all right elements at the same time.
                        # left: (0, 8)
                        # right: (1, 1), (2, 2)
                        smaller[left[-1][0]] += len(right) 
                        enum[i] = left.pop()
                    else:
                        # The order is correct
                        enum[i] = right.pop()
            return enum
            
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller
