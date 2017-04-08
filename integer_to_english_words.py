"""Convert a number into word in English

    << 123 
    => 'One Hundred Twenty Three'

    << 12345 
    => 'Twelve Thousand Three Hundred Forty Five'

    << 234567 
    => 'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven'
    
    << 0
    => 'Zero'

    - 12,345 Start with Twelve
    - No AND need

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve '\
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        thousands = 'Thousand Million Billion'.split()
        
        def words(num):
            
            if num < 20:
                return to19[num - 1:num]  # Avoid overflow to19[-1]
            if num < 100:
                return [tens[num / 10 - 2]] + words(num % 10)
            if num < 1000:
                return words(num / 100) + ['Hundred'] + words(num % 100)
            
            #                      words(1,234,567,890)
            # Skip Thousand, Million, until Billion
            # words(1) + Billion + words(234,567,890)
            #                      Skip Thousand utill Million
            #                      words(234) + Million + words(567,890)
            #                                        words(567) + Thousand + words(890)  
            for power, word in enumerate(thousands, 1):
                # Make sure every number in the loop is less than 1000
                                
                # Use a power above to check
                if num < 1000 ** (power + 1):                    
                    return words(num / 1000 ** power) + [word] + words(num % 1000 ** power)      
        
        return ' '.join(words(num)) or 'Zero'
    
num = 1234567890
print Solution().numberToWords(num)