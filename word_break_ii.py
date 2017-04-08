"""Given a string, return all possible sentences formed by the words in a dictionary.

    For example, given
    s = "catsanddog",
    dict = ["cat", "cats", "and", "sand", "dog"].

    A solution is ["cats and dog", "cat sand dog"].

    - For each matching word, match the rest to the end. (TLE)

    - Preppend the first word to all valid sentence (Permutation)

Time: O(mn)
Space:
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def helper(string, memo={}):
            if string in memo:
                return memo[string]

            if not string:
                return ['']

            ret = []
            for word in wordDict:
                if word == string[:len(word)]:
                    sentences = helper(string[len(word):], memo)

                    for sentence in sentences:
                        ret += word + (' ' if sentence else '') + sentence,

            memo[string] = ret
            return memo[string]
                
        return helper(s)

    def wordBreakTLE(self, s, wordDict):
        def helper(string, sentences, attemp=[]):
            if not string and attemp:
                sentences += ' '.join(attemp),
                return

            for word in wordDict:
                if word == string[:len(word)]:
                    attemp += string[:len(word)],

                    helper(string[len(word):], sentences, attemp)

                    attemp.pop()

        sentences = []
        helper(s, sentences)
        return sentences

chars = 'dropboxs'
dictionary = ['drop', 'box', 'bot']

def varify(chars):
    if not chars:
        return False

    def helper(chars):
        if not chars:
            return True

        for word in dictionary:
            n = len(word)
            if word == chars[:n]:
                if helper(chars[n:]):
                    return True

        return False

    return helper(chars)

print varify(chars)
