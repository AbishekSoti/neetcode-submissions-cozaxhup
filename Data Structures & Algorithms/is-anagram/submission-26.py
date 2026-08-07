class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_dict = {}
        for i in range(0,len(s)):
            if s[i] not in word_dict:
                word_dict[s[i]] =1
            else:
                word_dict[s[i]] +=1
        
        for j in range(0,len(t)):
            if t[j] not in word_dict:
                return False
            else:
                word_dict[t[j]] -=1
        
        # all individual values must be zero.

        if any(word_dict.values()) != 0:
            return False
        else:
            return True
