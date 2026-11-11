class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def dfs(subset):

            if len(subset) == len(nums):
                result.append(subset.copy())
                return

            for num in nums:
                is_num = False
                for i in subset:
                    if num == i:
                        is_num = True
                        break
                if is_num:
                    continue
                subset.append(num)
                dfs(subset)
                subset.pop()

        dfs([])
        return result

        
        