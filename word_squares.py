"""Return all valid word squares given words

    << ["area","lead","wall","lady","ball"]

    =>
    [
      [ "wall",
        "area",
        "lead",
        "lady"
      ],
      [ "ball",
        "area",
        "lead",
        "lady"
      ]
    ]

wall      Try words      wall                     wall                      wall
a...   => starting  =>   area      Try words      area                      area
l...      with "a"       le..   => starting  =>   lead      Try words       lead
l...                     la..      with "le"      lad.   => starting   =>   lady
                                                            with "lad"
    
Time: O(n^2)
Space: O(n) for the prefix dict

"""
from collections import defaultdict


class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        # Build a prefix dict. Since the length of each word is bounded to 5,
        # we can say this take O(cn) time.
        n = len(words[0])
        prefix = defaultdict(list)

        for word in words:
            for i in range(n):
                prefix[word[:i]].append(word)

        def build(rows):
            if len(rows) == n:
                squares.append(rows)
                return

            # a, le, lad, ...
            # *[[1, 2], [3, 4]] => [(1, 3), (2, 4)]
            target = ''.join(zip(*rows)[len(rows)])

            for word in prefix[target]:
                build(rows + [word])

        squares = []

        for word in words:
            build([word])

        return squares
