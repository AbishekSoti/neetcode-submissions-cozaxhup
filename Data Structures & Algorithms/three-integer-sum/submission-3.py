class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # has to be 3 only, not 1 sum 2 sum then 3 sum. 3 poitners.
        nums.sort()

        final_list = []
        for a in range(len(nums)-2):

            if a > 0 and nums[a] == nums[a-1]:
                continue  

            b=len(nums)-1
            c= a+ 1

            while c<b:

                if nums[a]+nums[b]+nums[c] == 0:
                    final_list.append([nums[a],nums[b],nums[c]])
                    b-=1
                    c+=1

                    while c < b and nums[c] == nums[c-1]:
                            c += 1
                elif nums[a]+nums[b]+nums[c]>= 0:
                    b-=1
                elif nums[a]+nums[b]+nums[c]<= 0:
                    c+=1

        return final_list
