class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
                # Method 3: one dict, make one dict then remove from it from second string value
        dict_primary = {}
        for item in s:
            if item not in dict_primary:
                dict_primary[item] = 1
            else:
                dict_primary[item] +=1
        print(dict_primary)
        for item in t:
            if item not in dict_primary:
                return False
            else:
                dict_primary[item] -=1
        print(dict_primary)
        return all(v==0 for v in dict_primary.values())