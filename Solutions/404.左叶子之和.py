#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# https://leetcode-cn.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (54.11%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    21.6K
# Total Submissions: 39.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 计算给定二叉树的所有左叶子之和。
# 
# 示例：
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
# 
# 
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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def sum(node, isLeft, counter):
            if not node:
                return
            if not node.left and not node.right and isLeft:
                counter[0] += node.val
            sum(node.left, True, counter)
            sum(node.right, False, counter)
        
        res = [0]
        sum(root, False, res)
        return res[0]
        
# @lc code=end

