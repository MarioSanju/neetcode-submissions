class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        self.total_suma = 0


        def dfs(index: int, actual_xor: int):

            if index == len(nums):
                self.total_suma += actual_xor
                return
            
            dfs(index + 1, actual_xor ^ nums[index])
            dfs(index + 1, actual_xor)
        
        dfs(0,0)
        return self.total_suma
            


        