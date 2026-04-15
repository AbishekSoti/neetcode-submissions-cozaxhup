class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        first_word = strs[0]

        shortestlength= len(first_word)
        for i in range(0,len(strs)):
            # use whichevers shorter, or pop to make equal.
            if shortestlength > len(strs[i]):
                shortestlength=len(strs[i])
                first_word =first_word[:shortestlength]
                print(first_word)

            for j in range(0,len(first_word)):
                print(j)
                if first_word[j]!=strs[i][j]:
                    #drop the letter from the list.
                    first_word = first_word[:j]
                    break
                    if len(first_word) == 0:

                        return ""
        return first_word
            