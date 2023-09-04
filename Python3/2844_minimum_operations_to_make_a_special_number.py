# https://leetcode.com/problems/minimum-operations-to-make-a-special-number/description/

class Solution:
    def minimumOperations(self, num: str) -> int:
        fivefound = False
        zerofound = False
        length = len(num)

        for i in range(length - 1, -1, -1):
            if zerofound and num[i] == '0':
                return length - 2 - i
            if zerofound and num[i] == '5':
                return length - 2 - i
            if fivefound and num[i] == '2':
                return length - 2 - i
            if fivefound and num[i] == '7':
                return length - 2 - i
            if num[i] == '5':
                fivefound = True
            if num[i] == '0':
                zerofound = True

        if zerofound:
            return length - 1
        
        return length
