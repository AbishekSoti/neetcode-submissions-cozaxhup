class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s,t = sorted(s), sorted(t)
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        
        # # method 2
        # dict_s = {}

        # for item in s:
        #     if item not in dict_s:
        #         dict_s[item] = 1
        #     else:
        #         dict_s[item] +=1
        # print(dict_s)

        # dict_t = {}
        # for item in t:
        #     if item not in dict_t:
        #         dict_t[item] = 1
        #     else:
        #         dict_t[item] +=1
        # print(dict_t)
        # if dict_t == dict_s:
        #     return True
        # else:
        #     return False

        # # Method 3: one dict, make one dict then remove from it from second string value
        # dict_primary = {}
        # for item in s:
        #     if item not in dict_primary:
        #         dict_primary[item] = 1
        #     else:
        #         dict_primary[item] +=1
        # print(dict_primary)
        # for item in t:
        #     if item not in dict_primary:
        #         return False
        #     else:
        #         dict_primary[item] -=1
        # print(dict_primary)
        # return all(v==0 for v in dict_primary.values())

        