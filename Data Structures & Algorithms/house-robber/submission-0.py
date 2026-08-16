from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def rob(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + rob(i+2), rob(i+1))
        return rob(0)

