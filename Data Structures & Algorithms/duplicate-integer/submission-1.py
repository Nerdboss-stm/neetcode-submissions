class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_dup = set()
        for i in nums:
            if i in non_dup:
                return True
            non_dup.add(i)
        return False
        