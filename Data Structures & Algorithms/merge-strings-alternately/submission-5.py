class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        shorter_word = word1 if len(word1)<len(word2) else word2
        longer_word = word1 if len(word1)>len(word2) else word2
        print(len(word1),len(word2))
        i = 0
        final_word = ""
        while i <len(shorter_word):
            final_word+=word1[i]+word2[i]
            i+=1
        
        print(i)
        print(longer_word[i:])
        to_add = longer_word[i:]
        final_word+=to_add

        # final_word

        return final_word