# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        
        for letter in s:
            if not letter in s_dict:
                s_dict[letter] = 1
            else:
                s_dict[letter] += 1
                
        for letter in t:
            if not letter in s_dict or s_dict[letter] <= 0:
                return False
            else:
                s_dict[letter] -= 1
        
        for key in s_dict:
            if s_dict[key] > 0:
                return False
        
        return True
