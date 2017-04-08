class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        strings = []
        for num in range(1, n + 1):
            if num % 15 == 0:
                strings.append('FizzBuzz')
            elif num % 5 == 0:
                strings.append('Buzz')
            elif num % 3 == 0:
                strings.append('Fizz')
            else:
                strings.append(str(num))
        return strings
