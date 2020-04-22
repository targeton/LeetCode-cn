#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#
# https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (58.67%)
# Likes:    60
# Dislikes: 0
# Total Accepted:    10K
# Total Submissions: 16.8K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# 您需要在二叉树的每一行中找到最大的值。
# 
# 示例：
# 
# 
# 输入: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \  
# ⁠     5   3   9 
# 
# 输出: [1, 3, 9]
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
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, q = [], [root]
        while q:
            tmp, ma = [], float('-inf')
            for n in q:
                ma = max(ma, n.val)
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            res.append(ma)
            q = tmp
        return res

# @lc code=end

