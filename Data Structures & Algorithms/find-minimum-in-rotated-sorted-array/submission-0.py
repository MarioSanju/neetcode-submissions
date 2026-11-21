class Solution:
    def findMin(self, nums: List[int]) -> int:

        minimum = float("inf")
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r)//2
            minimum = min(minimum, nums[mid])

            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return minimum

        

            

                    