class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen = set()
        longest_subString=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            length = right-left+1
            longest_subString = max(longest_subString,length)
        return longest_subString


        