# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        left = root
        right = root
        lp = rp = 0

        while left:
            lp +=1
            left = left.left

        while right:
            rp += 1
            right = right.right

        if lp == rp:
            return (1 << lp) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)