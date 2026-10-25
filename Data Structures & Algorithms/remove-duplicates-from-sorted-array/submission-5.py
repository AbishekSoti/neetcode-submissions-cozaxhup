class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=1
        for b in range(1,len(nums)):
            if nums[b] != nums[b-1]: # if no duplicates
                nums[a] = nums[b]
                a+=1
        return a