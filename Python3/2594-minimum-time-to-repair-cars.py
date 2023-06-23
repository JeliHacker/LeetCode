# https://leetcode.com/problems/minimum-time-to-repair-cars/description/

from math import sqrt
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
            
        low, high = 0, int(1e14)
        while low < high:
            mid = low + (high - low) // 2
            repaired_cars = sum(int(sqrt(mid // r)) for r in ranks)
            if repaired_cars < cars:
                low = mid + 1
            else:
                high = mid
        return low

