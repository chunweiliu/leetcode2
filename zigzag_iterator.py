"""Iterator two number list alternatively

    v1 = [1, 2]
    v2 = [3, 4, 5, 6]

    => (1, 3, 2, 4, 5, 6)

    * Do not use label to point to Integer
    * Empty inputs

Time:
    init: O(1)
    next: O(1)
    hasNext: O(1)
Space: O(n)
"""

class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vectors = []
        self.pointers = []
        
        if v1:
            self.vectors.append(v1)
            self.pointers.append(0)
            
        if v2:
            self.vectors.append(v2)
            self.pointers.append(0)
            
        self.count = 0

    def next(self):
        """
        :rtype: int
        """
        pointers = self.pointers
        vectors = self.vectors

        if self.hasNext():
            # An index that run-robin through the pointers
            i = self.count % len(pointers)

            v = vectors[i][pointers[i]]
            
            pointers[i] += 1

            if pointers[i] == len(vectors[i]):
                del pointers[i]
                del vectors[i]

            self.count += 1

            return v
            
    def hasNext(self):
        """
        :rtype: bool
        """
        return any(pointer < len(vector) 
                   for pointer, vector in zip(self.pointers, self.vectors))
        

# Your ZigzagIterator object will be instantiated and called as such:
# v1 = [1, 2]
# v2 = [3, 4, 5, 6]
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())