from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def climb(i):
            if i >= n:
                return i == n
            return climb(i+1) + climb(i+2)
        return climb(0)