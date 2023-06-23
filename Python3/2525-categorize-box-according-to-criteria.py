# https://leetcode.com/problems/categorize-box-according-to-criteria/description/

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height

        bulky = False
        heavy = False

        if mass >= 100:
            heavy = True

        if length >= 10000 or width >= 10000 or height >= 10000 or volume >= 1000000000:
            bulky = True

        if bulky and heavy:
            return "Both"
        elif (not bulky) and (not heavy):
            return "Neither"
        elif bulky and (not heavy):
            return "Bulky"
        else:
            return "Heavy"

        return "error"
