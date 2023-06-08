# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = [[] for _ in range(len(nums) + 1)]

        numbers = collections.defaultdict()

        print(numbers)

        for num in nums:
            numbers[num] = (numbers.get(num, 0)) + 1

        for key in numbers:
            frequencies[numbers[key]].append(key)

        print(numbers)
        print(frequencies)

        count = len(frequencies) - 1
        answer = []
        for i in range(k):
            while frequencies[count] == []:
                frequencies.pop(count)
                count -= 1
                
            append_this = frequencies[count].pop(0) 
            answer.append(append_this)

        return answer
