class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        final_large_list = []
        for every_word in strs:
            if str(sorted(every_word)) not in anagram_dict:
                anagram_dict[str(sorted(every_word))] = []
            anagram_dict[str(sorted(every_word))].append(every_word)
        print(anagram_dict.values())
        return list(anagram_dict.values())