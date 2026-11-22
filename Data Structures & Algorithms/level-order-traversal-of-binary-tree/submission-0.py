# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        q = deque()
        if root:
            q.append(root)

        while q:
            res = []

            for _ in range(len(q)):

                node = q.popleft()
                res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(res.copy())
        
        return result
                




        