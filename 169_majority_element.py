# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
            
        majorityNum = nums[0]
        
        for num in nums_dict:
            if nums_dict[num] > nums_dict[majorityNum]:
                majorityNum = num
                
        return majorityNum
