class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ordered_dict = {}
        for i in range(0,len(nums)):
            if nums[i] not in ordered_dict:
                ordered_dict[nums[i]] = 1
            else:
                ordered_dict[nums[i]] +=1
        print(ordered_dict)

        # Create a list with index as the keys( no index = empty list) and values would be the frequency.
        frequency = [[] for x in range(len(nums)+1)]
        print(frequency)
        for key,value in ordered_dict.items():
            frequency[value].append(key)
        print(frequency)

        empty_bucket = []       
        for i in reversed(frequency):
            if i is not []:
                empty_bucket+=i
        return empty_bucket[:k]
