#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#
# https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/description/
#
# algorithms
# Easy (46.19%)
# Likes:    183
# Dislikes: 0
# Total Accepted:    37.4K
# Total Submissions: 78.7K
# Testcase Example:  '[2,2,5,null,null,5,7]'
#
# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或
# 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
# 
# 更正式地说，root.val = min(root.left.val, root.right.val) 总成立。
# 
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [2,2,5,null,null,5,7]
# 输出：5
# 解释：最小的值是 2 ，第二小的值是 5 。
# 
# 
# 示例 2：
# 
# 
# 输入：root = [2,2,2]
# 输出：-1
# 解释：最小的值是 2, 但是不存在第二小的值。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 25] 内
# 1 
# 对于树中每个节点 root.val == min(root.left.val, root.right.val)
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        ans, rootval = -1, root.val
        
        def dfs(node):
            nonlocal ans
            if not node:
                return
            if ans != -1 and node.val > ans:
                return
            if node.val > rootval:
                ans = node.val
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ans
# @lc code=end

