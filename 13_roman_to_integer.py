# https://leetcode.com/problems/roman-to-integer/

# Original solution

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        
        string_list = list(s)
        
        index = 0
        
        numeral_instances = {
            "I": 0,
            "X": 0,
            "C": 0
        }
        
        numeral_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        while index < len(string_list):
            roman_numeral = s[index]
            
            if roman_numeral == "I" and (index + 1) < len(s):
                if s[index+1] == "V":
                    total += 4
                    index += 1
                
                elif s[index+1] == "X":
                    total += 9
                    index += 1
                    
                else:
                    total += numeral_values[roman_numeral]
                    
            elif roman_numeral == "X" and (index + 1) < len(s):
                if s[index+1] == "L":
                    total += 40
                    index += 1
                
                elif s[index+1] == "C":
                    total += 90
                    index += 1
                    
                else:
                    total += numeral_values[roman_numeral]
                    
            elif roman_numeral == "C" and (index + 1) < len(s):
                if s[index+1] == "D":
                    total += 400
                    index += 1
                
                elif s[index+1] == "M":
                    total += 900
                    index += 1
                    
                else:
                    total += numeral_values[roman_numeral]
                    
            else:
                total += numeral_values[roman_numeral]
            
            index += 1
            
        return total
            
