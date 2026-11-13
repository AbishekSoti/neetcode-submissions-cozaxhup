class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = nums
        for i in range(len(sum_dict)-1):
            j = i + 1
            while i <= len(sum_dict)-1:
                if sum_dict[i] + sum_dict[j] == target:
                    return [i,j]
                j += 1
                if j >= len(sum_dict): 
                    break 