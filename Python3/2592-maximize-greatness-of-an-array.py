# https://leetcode.com/problems/maximize-greatness-of-an-array/

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        sorted_nums = nums
        sorted_nums.sort()
        print(sorted_nums)
        nums_dict = {}
        perm = sorted_nums
        
        for num in nums:
            nums_dict[num] = 1 + nums_dict.get(num, 0)
        
        print(nums_dict)
        answer = 0
        
        for i in range(len(sorted_nums)):
            print(i)
            for key in nums_dict.keys():
                if key > sorted_nums[i]:
                    answer += 1
                    perm[i] = key
                    nums_dict[key] -= 1
                    if nums_dict[key] == 0:
                        del nums_dict[key]
                    break
        
        return answer
