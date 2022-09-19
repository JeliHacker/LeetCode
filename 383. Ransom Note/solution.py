class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomLetters = {}
        magazineLetters = {}
        
        for letter in magazine:
            if letter in magazineLetters:
                magazineLetters[letter] += 1
            else:
                magazineLetters[letter] = 1
            
        for letter in ransomNote:
            if letter in magazineLetters:
                if magazineLetters[letter] > 0:
                    magazineLetters[letter] -= 1
                else:
                    return False
            else:
                return False
        
        return True
