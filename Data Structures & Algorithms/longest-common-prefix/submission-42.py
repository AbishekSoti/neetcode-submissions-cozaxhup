class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        first_word = strs[0]


        for i in range(1,len(strs)):
            shortestlength= min(len(first_word), len(strs[i]))
            first_word = first_word[:shortestlength]
            for j in range(0,len(first_word)):
                if first_word[j]!=strs[i][j]:
                    #drop the letter from the list.
                    first_word = first_word[:j]
                    break

        return first_word
            