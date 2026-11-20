class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        maximum = 0
        
        for num in s:
            if num - 1 in s:
                continue
            counter = 1
            while num + counter in s:
                counter += 1
            maximum = max(maximum, counter)
        
        return maximum
        