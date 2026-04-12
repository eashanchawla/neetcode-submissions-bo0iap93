from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPileSize = max(piles) # O(n)
        left, right = 1, maxPileSize
        minBPH = float('inf')
        while left <= right:
            current_bph = (left + right) // 2
            current_time_to_eat = self.calculateTimeToEat(piles, current_bph)
            if current_time_to_eat > h:
                # we are too slow, so need to speed up 
                left = current_bph + 1 
            else:
                # acceptable speed, let's try to be slower
                # save first 
                minBPH = min(minBPH, current_bph)
                right = current_bph - 1
        return minBPH

    def calculateTimeToEat(self, piles: List[int], bph: int) -> int:
        return sum([ceil(pile / bph) for pile in piles])