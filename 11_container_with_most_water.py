# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute Force solution:
        # answer = 0
        
        # for left in range(len(height)):
        #     for right in range(left + 1, len(height)):
        #         area = (right - left) * min(height[left], height[right])
        #         answer = max(answer, area)

        # return answer


        # O(n) solution
        answer = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            answer = max(answer, area)
            smallerHeight = 0
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return answer

