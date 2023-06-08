# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Simplest Brute-Force solution.
        # Time complexity: O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         looking_for = target - nums[i]
        #         if nums[j] == looking_for:
        #             return [i, j]
        
        
        # Faster solution
        # Time complexity: O(n)
        # As we go through the list, we store numbers we've seen in a dictionary.
        # We store the number as the key and it's index as the value.
        numbers_seen = {}
        
        for i in range(len(nums)):
            looking_for = target - nums[i]
            if looking_for in numbers_seen:
                return [i, numbers_seen[looking_for]]
            else:
                numbers_seen[nums[i]] = i
                
        
