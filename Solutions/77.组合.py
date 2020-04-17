#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (73.19%)
# Likes:    249
# Dislikes: 0
# Total Accepted:    45.1K
# Total Submissions: 61.4K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 
# 示例:
# 
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(first=1, tmp=[]):
            if len(tmp) == k:
                res.append(tmp[:])
                return
            for i in range(first, n+1):
                tmp.append(i)
                backtrack(i+1, tmp)
                tmp.pop()

        backtrack()
        return res
        
# @lc code=end

