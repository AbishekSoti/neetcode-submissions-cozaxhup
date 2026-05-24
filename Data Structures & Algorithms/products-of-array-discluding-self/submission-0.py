class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        left_multiple = 1
        # 1 2 4 6
        for i in range(0,len(nums)):
            if i>0:
                left_multiple *=nums[i-1]
                output[i] *= left_multiple

        right_multiple = 1

        for j in range(len(nums)-2,-1,-1):

            if j< len(nums):
                right_multiple *=nums[j+1]
                output[j] *=right_multiple
        print(output)
        return output
                