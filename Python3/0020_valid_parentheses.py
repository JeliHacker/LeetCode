# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []

        bracket_dict = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for character in s:
            if character in bracket_dict:
                if len(bracket_stack) == 0:
                    return False
                else:
                    top_char = bracket_stack.pop()
                    if top_char != bracket_dict[character]:
                        return False
                
            else:
                bracket_stack.append(character)

        if len(bracket_stack) > 0:
            return False
        else:
            return True
