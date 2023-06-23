# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        
        for letter in s:
            if letter == "#":
                if len(s_stack) <= 0:
                    pass
                else:
                    s_stack.pop()
            else:
                s_stack.append(letter)
                
        t_stack = []
        
        for letter in t:
            if letter == "#":
                if len(t_stack) <= 0:
                    pass
                else:
                    t_stack.pop()
            else:
                t_stack.append(letter)   
                
        s_joined = "".join(s_stack)
        t_joined = "".join(t_stack)
        
        return s_joined == t_joined
            
