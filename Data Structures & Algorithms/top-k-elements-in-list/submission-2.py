class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ordered_dict = {}
        for i in range(0,len(nums)):
            if nums[i] not in ordered_dict:
                ordered_dict[nums[i]] = 1
            else:
                ordered_dict[nums[i]] +=1
        
        #print(ordered_dict,k)

        #print(ordered_dict.items())
        new_list=[]
        new_list = ordered_dict.items()
        new_list = sorted(new_list, key = lambda x: x[1], reverse = True)
        #print(new_list)
        return [x[0] for x in new_list[:k]]

