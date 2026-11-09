class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        k = k%len(nums)
        # 1st half
        i=0
        c = k-1

        while i<c:
        
            nums[i], nums[c] = nums[c],nums[i]
            i+=1
            c-=1

        
        a = k
        b = len(nums)-1
        while a < b:
            nums[a], nums[b] = nums[b], nums[a]
            a+=1
            b-=1

