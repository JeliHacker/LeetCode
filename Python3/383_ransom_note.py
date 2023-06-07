# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        
        for letter in magazine:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        
        
        
        for letter in ransomNote:
            if letter in letters:
                if letters[letter] > 0:
                    letters[letter] -= 1
                else:
                    return False
            else: 
                return False
        
        return True
