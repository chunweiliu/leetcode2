"""Given a pattern and a string str, find if str follows the same pattern.

    pattern = "abba", str = "dog cat cat dog" should return true.

    pattern = "abba", str = "dog cat cat fish" should return false.

    * pattern = "ab", str = "dog dog" should return false.

    * pattern = "abc", str = "b c a" should return true.

    - True if and only if the pattern and string are one to one mapping

          ----------- len
          v
      s:  A    B    C

      t:  a    b    c
          ^
         zip

    - Index check

        * Only work in Java, since java char and string are in different class.

Time: O(n)
Space: O(n)
"""

class Solution(object):
    def wordPatternJavaOnly(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')

        if len(pattern) != len(words):
            return False

        # latest index for the alpha
        index = {}
        for i, (char, word) in enumerate(zip(pattern, words)):
            if char in index and word in index:
                if index[char] != index[word]:
                    return False
                index[char] = index[word] = i
            elif char in index or word in index:
                return False
            else:
                index[char] = index[word] = i

        return True


    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split(' ')

        # one to one mapping
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
