class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = ""
        i=0
        if len(word1) < len(word2):
            shortest_length = len(word1)
            shortest_word = word1
            longest_word = word2
        else:
            shortest_length = len(word2)
            shortest_word = word2
            longest_word = word1
        
        while i <shortest_length:
            new_word += word1[i]+word2[i]
            i+=1
        while i<len(longest_word):
            new_word+=longest_word[i]
            i+=1
        return new_word
