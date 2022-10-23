# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        characters_dict = {")":"(", "}":"{", "]":"["}
        
        for letter in s:
            if letter in characters_dict.values():
                my_stack.append(letter)
            elif letter in characters_dict.keys():
                if my_stack == [] or characters_dict[letter] != my_stack.pop():
                    return False
               
        if my_stack != []:
            return False
        else:
            return True
            
                
