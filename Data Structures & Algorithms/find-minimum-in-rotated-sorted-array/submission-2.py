class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:                   # < not <=  : we CONVERGE on the answer
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:     # above the right end -> cliff is to my right
                lo = mid + 1             # the min is right of me; I can't be it
            else:                        # clean slope from me to the right end
                hi = mid                 # cliff is at me or left; KEEP mid
        return nums[lo]