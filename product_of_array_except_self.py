"""Product without self
    
    <<     [1,  2,  3, 4]
    =>     [24, 12, 8, 6]
    
    1      1   2   6  24
    r      24  24  12  4 
    
    ls     1   1   2   6  24
    rs     24 24  12  4   1  
    
    Use accumlated products left and right,

    prod[i] = left[i - 1] * right[i + 1]
    
    
    
Time: O(n)
Space: O(n)
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def accumlated_products(nums):
            accumlated, products = 1, []
            
            for num in nums:
                accumlated *= num
                products.append(accumlated)
            
            return products
        
        lefts = accumlated_products(nums)
        rights = accumlated_products(nums[::-1])[::-1]
        
        results = [0] * len(nums)
    
        for i in range(len(results)):
            if i == 0:
                results[i] = rights[1]
            elif i == len(results) - 1:
                results[i] = lefts[-2]
            else:
                results[i] = lefts[i - 1] * rights[i + 1]
            
        return results