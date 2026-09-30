class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        k = len(nums1)-1 # locaiton pointer
        m-=1 # m =3
        n-=1 # n = 1
        # Input: nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2


        while m>=0 and n>=0:

            if nums1[m] > nums2[n]:
                nums1[k]= nums1[m]
                k-=1
                m-=1


            else:
                nums1[k] =nums2[n]
                k-=1
                n-=1
        
        while n>=0:
            nums1[k] = nums2[n]
            n-=1
            k-=1
        return nums1
                