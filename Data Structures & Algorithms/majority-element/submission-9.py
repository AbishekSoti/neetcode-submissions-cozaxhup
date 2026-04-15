class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {x:nums.count(x) for x in nums if nums.count(x)>=len(nums)/2}
        
        for key in count_dict:
            return key