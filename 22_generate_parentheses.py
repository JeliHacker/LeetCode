# https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n

        stack = []
        answer = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                answer.append("".join(stack))

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return answer


