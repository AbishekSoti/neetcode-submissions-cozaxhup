class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        first_value = None
        second_value = None
        first_value_count = 0
        second_value_count = 0
        for i in nums:
            if i == first_value:
                first_value_count+=1
            elif i == second_value:
                second_value_count+= 1
            elif first_value_count ==0:
                first_value = i
                first_value_count +=1
            elif second_value_count ==0:
                second_value =i
                second_value_count +=1
            else:
                first_value_count-= 1
                second_value_count-= 1

        print(first_value, second_value)
        return_list = []
        n = len(nums)
        # count to store for these top two numbers. 
        first_number = 0
        second_number= 0

        for i in nums:
            if i == first_value:
                first_number +=1
            if i == second_value:
                second_number +=1
        if first_number>n/3:
            return_list.append(first_value)
        if second_number>n/3:
            return_list.append(second_value)

        return return_list
            
        
