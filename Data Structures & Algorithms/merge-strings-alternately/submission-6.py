class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        i = 0
        right = 0

        answer = ""

        while i < len(word1) and i <  len(word2):
            answer += word1[i]
            answer += word2[i]
            i += 1

        answer += word1[i:] + word2[i:]

        return answer
