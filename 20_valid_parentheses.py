# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        
        inputs_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for letter in s:
            print(letter)
            if letter in inputs_dict:
                if len(my_stack) == 0 or my_stack.pop() != inputs_dict[letter]:
                    return False
            else:
                my_stack.append(letter)
                
        if len(my_stack) != 0:
            return False
        else:
            return True
        
