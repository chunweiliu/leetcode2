"""Return every combinations for a target

    123, 6 -> [1 + 2 + 3, 1 * 2 * 3]
    123, 9 -> []
    00, 0 -> [0 - 0, 0 + 0, 0 * 0]
   
T(n): (4^(n-1)) Since we can either try ['', '+', '-', '*'] between each digit.

Recursive descent parser with analysis:
    https://maskray.me/blog/2015-10-16-leetcode-expression-add-operators
"""
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        results = []

        def evaluator(digits, attemp='', total=0, multed=0):        
            if not digits and total == target:
                results.append(attemp)
                
            for length in range(1, len(digits) + 1):
                if length > 1 and digits[0] == '0':
                    break
                
                current, left = digits[:length], digits[length:]
                current_num = int(current)
                
                # Not append any opperator
                if not attemp:                
                    evaluator(left, current, current_num, current_num)
                # Need to append the operator
                else:
                    # 2 + 3 * 4 * 5
                    # ---------
                    # 14
                    # -------------
                    # 14 - 12 + 12 * 5
                    evaluator(left, attemp + '*' + current,
                              (total - multed) + multed * current_num, multed * current_num)
                    
                    evaluator(left, attemp + '+' + current,
                              total + current_num, current_num)
    
                    evaluator(left, attemp + '-' + current,
                              total - current_num, -current_num)
        
        evaluator(num)
        return results