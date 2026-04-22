class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp_value = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[j]<nums[i]:
                    temp_value = nums[j]
                    nums[j] =nums[i]
                    nums[i] = temp_value
                
        return nums                
            