# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = ''
        carry = 0
        
        a = a[::-1]
        b = b[::-1]
        
        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0
            
            currentTotal = digitA + digitB + carry
            char = str(currentTotal % 2)
            answer = char + answer
            carry = currentTotal // 2
            
        while carry > 0:
            answer = str(carry % 2) + answer
            carry = carry // 2
            
        return answer
    
