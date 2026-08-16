from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(maxsize=None)
        def climb(i):
            if i >= len(cost):
                return 0 
            return cost[i] + min(climb(i+1), climb(i+2))
        return min(climb(0), climb(1))
        