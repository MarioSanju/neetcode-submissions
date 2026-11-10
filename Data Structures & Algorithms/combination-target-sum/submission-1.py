class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        def dfs(index: int, subset: list, actual_sum: int):
            if actual_sum == target:
                result.append(subset.copy())
                return

            if actual_sum > target or index == len(nums):
                return

            subset.append(nums[index])
            dfs(index, subset, actual_sum + nums[index])
            subset.pop()
            dfs(index + 1, subset, actual_sum)
        
        dfs(0, [], 0)
        return result

        