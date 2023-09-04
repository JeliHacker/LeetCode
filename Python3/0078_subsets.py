def subsets(nums: list[int]) -> list[list[int]]:
    answer = []

    subset = []
    def dfs(i):
        if i >= len(nums):
            print(subset)
            answer.append(subset.copy())
            return

        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)

        # decision NOT to include nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return answer

print(subsets([1,2]))
