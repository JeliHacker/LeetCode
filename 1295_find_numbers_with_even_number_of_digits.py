# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            num_list = list(str(num))
            if len(num_list) % 2 == 0:
                answer += 1
                
        return answer
