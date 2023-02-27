# https://leetcode.com/problems/minimum-score-by-changing-two-elements/description/

class Solution:
    def minimizeSum(nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        return min(
            abs(nums[n - 3] - nums[0]),
            abs(nums[n - 2] - nums[1]),
            abs(nums[n - 1] - nums[2])
        )
    
