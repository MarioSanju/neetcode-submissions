class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sequence = set()
        longest = 0
        l = 0
        r = 0

        for char in s:
            while char in sequence:
                sequence.remove(s[l])
                l += 1
            r += 1
            longest = max(longest, r - l)
            sequence.add(char)
        
        return longest




        