class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # odd vs even. might not matter
        start = 0
        end = len(s)-1
        i = 0
        # only need to iterate half time. while loop.
        while start!=end and start<end:
            s[start],s[end] = s[end],s[start]
            start+=1
            end-=1

        return s
        