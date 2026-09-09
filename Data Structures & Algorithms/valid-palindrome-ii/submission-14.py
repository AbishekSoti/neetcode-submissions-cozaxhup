class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        def palindrome_checker(start,end) -> bool:
            while start<end:
                if s[start] ==s[end]:
                    start+=1
                    end-=1
                else:
                    return False
            return True

        while start < end:
            if s[start] == s[end]:
                start+=1
                end-=1
            else:
                return palindrome_checker(start+1,end) or palindrome_checker(start,end-1)

        return True
