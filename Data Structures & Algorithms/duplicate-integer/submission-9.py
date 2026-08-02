class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_list = []
        for i in nums:
            if i not in unique_list:
                unique_list.append(i)

        return len(unique_list) != len(nums)         