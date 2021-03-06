#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (37.59%)
# Likes:    193
# Dislikes: 0
# Total Accepted:    13.8K
# Total Submissions: 36.7K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空二叉树，返回其最大路径和。
# 
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# 输出: 6
# 
# 
# 示例 2:
# 
# 输入: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# 输出: 42
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ma = float('-inf')
        def maxSum(node):
            nonlocal ma
            if not node:
                return 0
            l, r = maxSum(node.left), maxSum(node.right)   
            large = max([l, r, l+r])
            ma = max(node.val+large if large > 0 else node.val, ma)
            return node.val + max(l,r) if max(l,r) > 0 else node.val
        maxSum(root)
        return ma
# @lc code=end

