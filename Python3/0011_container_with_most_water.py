# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        answer = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            answer = max(answer, area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
        return answer
