# https://leetcode.com/problems/combinations/description/


def combine(n: int, k: int) -> list[list[int]]:
    answer = []

    def backtrack(start: int, my_combination: list) -> list[int]:
        if len(my_combination) == k:
            answer.append(my_combination.copy())
            return

        for i in range(start, n + 1):
            my_combination.append(i)
            backtrack(i + 1, my_combination)
            my_combination.pop()
        
    backtrack(1, [])
    return answer

n = 4
k = 2

print(combine(n, k))

