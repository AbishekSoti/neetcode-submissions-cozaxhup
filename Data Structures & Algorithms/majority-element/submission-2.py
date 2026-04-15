class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        len_num_half= len(nums)/2
        for i in nums:
            if nums.count(i) >= len_num_half:
                nums_dict[i] = nums.count(i)
        for key in nums_dict:
            return key
