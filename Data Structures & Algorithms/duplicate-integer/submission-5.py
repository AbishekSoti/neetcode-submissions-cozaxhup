class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set(nums)
        print(unique_nums)
        return len(nums) != len(unique_nums)

        # Solution i later learned from chatgpt(same worst case scenario, but better best case)
        # seen = set()
        # for nums in nums:
        #     if nums in seen:
        #         return True
        #     seen.add(num)
        # return False

            