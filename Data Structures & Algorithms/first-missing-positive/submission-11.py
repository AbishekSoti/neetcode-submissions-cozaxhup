class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lnums = len(nums)
        nums = set(nums)
        for i in range(1,lnums+1):
            if i not in nums:
                return i
        return lnums+1