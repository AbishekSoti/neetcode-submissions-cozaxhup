class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_list = []
        for i in nums:
            if i in unique_list:
                return True
            else:
                unique_list.append(i)
        return False
      