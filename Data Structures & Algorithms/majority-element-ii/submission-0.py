class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        n = len(nums)
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                nums_dict[i]+=1
        print(nums_dict)
        nums_dict
        final_list = []

        for key, value in nums_dict.items():
            if value> n/3:
                final_list.append(key)
        return final_list
