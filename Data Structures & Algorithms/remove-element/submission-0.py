class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # check if var is equal to that nums value
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
        return len(nums)

                