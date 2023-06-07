# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [0 for n in nums]
        
        dp[0] = nums[0]
        answer = dp[0]
        
        for i in range(1, len(nums)):
            print(answer)
            if dp[i - 1] > 0:
                dp[i] = nums[i] + dp[i - 1]
            else:
                dp[i] = nums[i]
                
            answer = max(answer, dp[i])
            
        return answer
        

