class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s,t = sorted(s), sorted(t)
        if sorted(s) == sorted(t): # and len(s) ==len(t):
            return True
        else:
            return False
        
        # method 2
        
        # for item in s:
        #     count = 0
        #     if item == item-1
        #     dict_s = {s:count}
        