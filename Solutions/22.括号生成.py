#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (73.61%)
# Likes:    974
# Dislikes: 0
# Total Accepted:    118.3K
# Total Submissions: 157.2K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例：
# 
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
# 
# 
#

# @lc code=start

# # iteration solution
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         candidates = [(n,n,'')]
#         res = []
#         while candidates:
#             item = candidates.pop(0)
#             if item[0] == item[1] == 0:
#                 res.append(item[2])
#                 continue
#             if item[0] <= item[1] and item[0] > 0:
#                 candidates.append((item[0]-1,item[1],item[2]+'('))
#             if item[0] < item[1] and item[0] >= 0:
#                 candidates.append((item[0], item[1]-1, item[2]+')'))
            
#         return res

# backtrack solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(l,r,res,cur):
            if l == 0 and r == 0:
                res.append(cur)
                return
            if l <= r and l > 0:
                generate(l-1, r, res, cur+'(')
            if l < r and l >= 0:
                generate(l, r-1, res, cur+')')
        
        res, cur = [], ''
        generate(n, n, res, cur)
        return res
# @lc code=end

