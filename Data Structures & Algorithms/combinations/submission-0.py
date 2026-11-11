class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []

        def dfs(index: int, subset: list, lenght: int):

            if lenght == k:
                result.append(subset.copy())
                return
            
            if index == n + 1:
                return
            

            subset.append(index)
            dfs(index + 1, subset, lenght + 1)
            subset.pop()
            dfs(index + 1, subset, lenght)

        dfs(1, [], 0)
        return result


        