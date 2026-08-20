class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        longest = 0
        # Calculator
        for num in snums:
            if num-1 not in snums:
                start_of_sequence = num-1
                length = 1
                while num+length in snums:
                    length+=1
                if length>longest:
                    longest = length
        return longest
                
        