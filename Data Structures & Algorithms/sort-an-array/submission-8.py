class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left,right):
            result = []
            i,j=0,0
            while i<len(left) and j <len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i+=1
 
                else:
                    result.append(right[j])
                    j+=1
 
            while i<len(left):
                result.append(left[i])
                i=i+1
            while j<len(right):
                result.append(right[j])
                j=j+1
            return result


        def merge_sort(nums): # Takes a list
            # keep calling it untill lift can no longer be splitted
            if len(nums)<=1:
                return nums

            left_list, right_list = nums[:len(nums)//2], nums[len(nums)//2:]

            left = merge_sort(left_list)
            right = merge_sort(right_list)

            return merge(left,right) 



        return merge_sort(nums)