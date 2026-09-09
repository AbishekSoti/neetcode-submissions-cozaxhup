class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = []
        i=0
        if len(word1) < len(word2):
            shortest_length = len(word1)
            longest_word = word2
        else:
            shortest_length = len(word2)
            longest_word = word1
        
        while i <shortest_length:
            new_word.append(word1[i])
            new_word.append(word2[i])
            i+=1
        while i<len(longest_word):
            new_word.append(longest_word[i])
            i+=1
        final_word = "".join(new_word)
        return final_word
