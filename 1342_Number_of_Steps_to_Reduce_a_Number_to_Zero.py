# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            # Before we used num % 2
            if (num & 1) == 0:
                # Before we used num = num / 2
                num = num >> 1
            else:
                num = num - 1
            steps += 1
        
        return steps
                
    
