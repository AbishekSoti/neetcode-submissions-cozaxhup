class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp_value = None
        for i in range(len(nums)):
            lowest_index =i

            for j in range(i,len(nums)):
                if nums[j]<nums[lowest_index]:
                    lowest_index = j                  
            # now we must put lowest index element at i location
            # but we cant just overwrite it so this doenst work:
            nums[i], nums[lowest_index] = nums[lowest_index], nums[i]



            

  
 
                
        return nums                
            