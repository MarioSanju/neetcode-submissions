class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()

        def dfs(index: int, actual_sum: int, subset: list):

            if actual_sum == target:
                result.append(subset.copy())
                return
            
            if actual_sum > target or index == len(candidates):
                return

            subset.append(candidates[index])
            dfs(index + 1, actual_sum + candidates[index], subset)
            subset.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            dfs(index + 1, actual_sum, subset)
        
        dfs(0, 0, [])
        return result
            


        