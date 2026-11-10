class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        def dfs(index: int, subset: list, actual_sum: int):
            if index == len(nums):
                return

            if actual_sum >= target:
                if actual_sum == target:
                    result.append(subset.copy())
                return

            subset.append(nums[index])
            dfs(index, subset, actual_sum + nums[index])
            subset.pop()
            dfs(index + 1, subset, actual_sum)
        
        dfs(0, [], 0)
        return result

        