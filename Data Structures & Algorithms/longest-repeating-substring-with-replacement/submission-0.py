class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hm = {}
        longest = 0
        l = 0 
        r = 0

        for char in s:
            if char in hm:
                hm[char] += 1
            else:
                hm[char] = 1
            
            r += 1

            max_frequency = 0
            for value in hm.values():
                max_frequency = max(max_frequency, value)

            needed_changes = (r - l) - max_frequency

            if k < needed_changes:
                hm[s[l]] -= 1
                l += 1
            
            else:
                longest = max(longest, r - l)
        
        return longest

                


        

        

        