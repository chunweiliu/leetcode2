"""Figure out if a word has a unique abbreviation

    Example of abbr.
        - internationalization = i18n

    Use a counter for the dictionary, return True if the abbrs is less than 2

    * The dictionary can have duplicates,
      such as ['a', 'a'], but 'a' has unique abbr.

    * The dictionary can have zero words,
      such as [], then any word has a unique abbr.

    * ['dog']
       'dig' => False, look up ['d1g'] = {'dog'}

Time: 
    - __init__: O(n)
    - isUnique: O(1)

Space: O(n)
"""
from collections import defaultdict


class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrs = defaultdict(set)
        for word in dictionary:
            self.abbrs[self.abbr(word)].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        same_abbrs = self.abbrs[self.abbr(word)]

        if len(same_abbrs) < 1 or (len(same_abbrs) == 1 and word in same_abbrs):
            return True
        return False

    def abbr(self, word):
        n = len(word)
        if n < 3:
            return word
        return word[0] + str(n - 2) + word[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")