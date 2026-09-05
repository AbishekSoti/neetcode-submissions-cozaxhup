class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}

        for i in range(0,len(strs)):
            
            sorted_i = sorted(strs[i])
            sorted_i = "".join(sorted_i)

            if sorted_i not in dicts:
                dicts[sorted_i] =[]

            dicts[sorted_i].append(strs[i])

        return list(dicts.values())
