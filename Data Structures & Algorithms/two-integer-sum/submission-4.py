class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums) - 1):
            for j in range(1,len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    return res

