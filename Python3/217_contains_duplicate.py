# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_seen = {}
        for i in nums:
            if i in nums_seen:
                return True
            else:
                nums_seen[i] = 1
                
        return False

