# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = sum(range(len(nums) + 1))

        sum2 = sum(nums)
        
        return sum1 - sum2
