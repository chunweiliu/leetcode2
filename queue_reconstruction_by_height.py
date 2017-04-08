"""Recontruct a queue, so the element in there satisify constraints:

    Each person is described by a pair of integers (h, k), 
    where h is the height of the person and k is the number of 
    people in front of this person who have a height greater than or equal to h.

    << [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    => [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


    Greedy:
        1. Sorted people by h. 
        2. Arrange highest people by their k value.
           (Insert that person into k)
        3. And then the second heightest person...

    7 0
    7 1
    6 1
    5 0
    5 2
    4 4

    [5, 7, 5, 6, 4, 7]

    * It works because higher person doesn't care people who is shorter than him.
      So, once the heightest person was insert to a position that satisify the constrants.
      The next person won't change that.
      
    * Sort need to aware the k as well, smaller k inserted first.

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = []
        for person in sorted(people, key=lambda (h, k): (-h, k)):
            position = person[1]
            queue.insert(position, person)
        return queue
