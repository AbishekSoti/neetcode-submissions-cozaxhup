class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        print(nums)
        fdict = dict()
        fdict[0] =1
        rolling_sum = 0
        frequency_counter = 0
        for i in nums:
            rolling_sum+=i

            if rolling_sum-k in fdict:
                frequency_counter +=fdict[rolling_sum-k]
                
            if rolling_sum not in fdict:
                fdict[rolling_sum] =1
            else:
                fdict[rolling_sum] +=1



        print(fdict)
        return frequency_counter
            