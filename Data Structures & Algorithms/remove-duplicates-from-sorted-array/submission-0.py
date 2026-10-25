class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        b = 1
        a= 0
        print(nums)
        lnums =len(nums)
        while b<=lnums-1:  
            if nums[a]==nums[b]: #if we dont find a duplicate,carry on.
                b+=1
            else:
                a+=1
                nums[a]=nums[b]
        print(nums)
        print(a,b)
        return a+1
            


          


