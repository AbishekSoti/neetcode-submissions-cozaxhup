class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        flist = []
        for a in range(0,len(nums)):
            for b in range(a+1, len(nums)):
                c = b+1
                d = len(nums)-1
                while d>c:
                    if nums[c] + nums[d] == target - nums[a] -nums[b]:
                        if [nums[a],nums[b],nums[c],nums[d]] not in flist:
                            flist.append([nums[a],nums[b],nums[c],nums[d]])
                        c+=1
                        d-=1
                    elif nums[c] + nums[d] >= target - nums[a] -nums[b]:
                    
                        d-=1
                    elif nums[c] + nums[d] <= target - nums[a] -nums[b]:
                        c+=1


        print(flist)
        return flist
