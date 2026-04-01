class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        # only add to dictionary based on a condition
        # If the target-number exists in the dictionary then we add it
        #to the diciotnary or we just return list indices???
        for i in range(len(nums)):
            if target - nums[i] not in d:
                d[nums[i]] =i
            else:
                return [d[target-nums[i]],i]
 
           
        
        