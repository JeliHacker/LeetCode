class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pastNumbers = {}
        for count, number in enumerate(nums):
            print(count, number)
            comp = target - number
            if comp in pastNumbers:
                return [count, pastNumbers[comp]]
            
            pastNumbers[number] = count
            
        return [-1,-1]
           


# My first solution that I wrote completely on my own. Granted, I had seen the solution before. 
