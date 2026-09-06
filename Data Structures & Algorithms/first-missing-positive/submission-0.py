class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        print(nums)
        # [-2,-1,0]

        for i in range(1,100000):
            if i not in nums:
                return i