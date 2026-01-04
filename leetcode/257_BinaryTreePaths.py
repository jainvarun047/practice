#!usr/bin/python3

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        if not root:
            return []
        
        paths = []

        def dfs(node, current_path):
            if node.left is None and node.right is None:
                paths.append(current_path)
                return
            
            if node.left:
                dfs(node.left, current_path + "->" + str(node.left.val))
            if node.right:
                dfs(node.right, current_path + "->" + str(node.right.val))

        dfs(root, str(root.val))
        return paths