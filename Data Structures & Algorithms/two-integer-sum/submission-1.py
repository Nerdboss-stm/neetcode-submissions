class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if i < j and i != j and nums[i] + nums[j] == target:
                    l.append(i)
                    l.append(j)
        return l        