# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        
        for letter in s:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
                
        length = 0
        odd_number_used = False
        
        for letter in letters:
            if letters[letter] % 2 == 1 and odd_number_used == False:
                odd_number_used = True
                length += letters[letter]
            else:
                if letters[letter] % 2 == 1:
                    length += (letters[letter] - 1)
                else:
                    length += (letters[letter])
                
            
        return length

