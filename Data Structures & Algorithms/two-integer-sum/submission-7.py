class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsd = {}
        for i in range(0,len(nums)):
            if target - nums[i] not in numsd:
                numsd[nums[i]] = i
            else:
                return [numsd[target-nums[i]],i]


    

