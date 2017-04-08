"""The definition of a celebrity is
    
    1) Everyone knows him/her, and
    2) He/she knows none of those people.

    - Is knows function symmetric?
    - Can a person know him/herself?
    - What if no one know each other, who is the celebrity then?

Algorithm:
    Given the definition, there is only ONE celebrity in the party.
    The candidate cannot known anyone. So if the current candidate
    know someone, he/she is not a celebrity and give the chance to
    next one.

    Verify the candidate is *not knowing anyone*

    Verify the candidate is *known by everyone*

Time: O(n)
Space: O(1)
"""

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: intr
        :rtype: int
        """
        # Given the definition, there is only ONE celebrity in the party.
        # The candidate cannot known anyone. So if the current candidate
        # know someone, he/she is not a celebrity and give the chance to
        # next one.
        candidate = 0
        for i in range(n):
            if knows(candidate, i):
                candidate = i

        # Verify the candidate is *not knowing anyone*
        if any(knows(candidate, i) for i in range(n) if i != candidate):
            return -1

        # Verify the candidate is *known by everyone*
        if not all(knows(i, candidate) for i in range(n) if i != candidate):
            return -1

        return candidate

    def find_celebrity_TLE(self, n):
        """
        Algorithms:
            Use a matrix to see the relationship for all pairs
            Time: O(n^2)
            Space: O(n^2)

        Example:
              0 1 2 3
            0 T T T T
            1 F T T T
            2 F F T F
            3 F F T T       
        """
        relationship = [[knows(i, j) for j in range(n)] for i in range(n)]

        for i in range(n):
            # If you know no one and everyone knows you, you are a celebrity.
            if all(not relationship[i][j] and relationship[j][i] for j in range(n) if i != j):
                return i

        return -1
