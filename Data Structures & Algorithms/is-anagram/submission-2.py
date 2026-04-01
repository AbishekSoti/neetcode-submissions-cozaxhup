class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s,t = sorted(s), sorted(t)
        if s == t: # and len(s) ==len(t):
            return True
        else:
            return False