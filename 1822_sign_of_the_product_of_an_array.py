# https://leetcode.com/problems/sign-of-the-product-of-an-array/

def arraySign(self, nums: List[int]) -> int:
        product = 1
        
        for num in nums:
            product *= num
            
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
