# https://leetcode.com/problems/combinations/description/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def backtrack(start: int, my_combination: list) -> List[int]:
            if len(my_combination) == k:
                answer.append(my_combination.copy())
                return

            for i in range(start, n + 1):
                my_combination.append(i)
                backtrack(i + 1, my_combination)
                my_combination.pop()
            
        backtrack(1, [])
        return answer

