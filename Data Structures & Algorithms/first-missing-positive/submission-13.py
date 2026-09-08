class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lnums = len(nums)
        #[-2,-1,0]
        a = 0 # pointer
        i = 0# counter variable
        # array: [3,4,5,6,1,2]
        #position[0,1,2,3,4,5]
        while i<len(nums):

            if nums[i]>0 and nums[i]<=len(nums):
                if nums[i]-1 !=i:
                    a= nums[i]-1
                    if nums[i]!= nums[a]:
                        nums[i], nums[a] = nums[a],nums[i]
                    else:
                        i+=1
                else:    
                    i +=1
            else:
                i+=1
    
        # array: [3,4,5,6,1,2]
        # sorted:[1,2,3,4,5,6]
        #position[0,1,2,3,4,5]
        #  sorted = position + 1
        # sorted-1 = position
        for i in range(0,len(nums)):
                if i != nums[i]-1:
                    return i+1

        
        return len(nums)+1

