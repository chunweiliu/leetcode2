"""Design a container for insert, remove, and removeRandom. All in O(1) average.

    ['a', 'b', 'c', 'd']
    {'a': 0, 'b': 1, 'c': 2, 'd': 3}

    delete 'b':
    - move 'b' to the end
    - give 'b' index to whatever element in the end

    ['a', 'd', 'c']
    {'a': 0, 'd': 1, 'c': 2}


Time: O(1)
Space: O(n)

Note: LinkedIn phone screen
"""
import random


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.index = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            return False

        self.nums.append(val)
        self.index[val] = len(self.nums) - 1

        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            return False

        nums = self.nums
        index = self.index

        # Pass the index to the last element, which is going to be swap
        i = index[val]
        index[nums[-1]] = i
        
        nums[i], nums[-1] = nums[-1], nums[i]

        nums.pop()
        del index[val]

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        i = random.randrange(len(self.nums))
        return self.nums[i]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()