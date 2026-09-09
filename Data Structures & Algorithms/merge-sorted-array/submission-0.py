class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(nums1,m)
        print(nums2, n)
        i = 0
        
        while i < n:
            nums1[m+i] = nums2[i]
            i+=1
        nums1.sort()
        print(nums1)