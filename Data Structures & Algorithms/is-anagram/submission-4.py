class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s,t = sorted(s), sorted(t)
        # if sorted(s) == sorted(t): # and len(s) ==len(t):
        #     return True
        # else:
        #     return False
        
        # method 2
        dict_s = {}

        for item in s:
            if item not in dict_s:
                dict_s[item] = 1
            else:
                dict_s[item] +=1


        dict_t = {}
        for item in t:
            if item not in dict_t:
                dict_t[item] = 1
            else:
                dict_t[item] +=1

        if dict_t == dict_s:
            return True
        else:
            return False
