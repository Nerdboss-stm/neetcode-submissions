class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:                 # Classic template : hunting a value
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:    #left half is the clean one
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1        # in the clean range -> search it
                else:
                    lo = mid + 1        # else it MUST be be in the messy half
            else:                       # right half is the clean one
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


        