#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
# https://leetcode-cn.com/problems/perfect-squares/description/
#
# algorithms
# Medium (54.82%)
# Likes:    360
# Dislikes: 0
# Total Accepted:    47.2K
# Total Submissions: 85.3K
# Testcase Example:  '12'
#
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# 
# 示例 1:
# 
# 输入: n = 12
# 输出: 3 
# 解释: 12 = 4 + 4 + 4.
# 
# 示例 2:
# 
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.
# 
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        s, index = set(), 1
        s.add(n)
        while len(s) > 0:
            ss = set()
            for i in s:
                m = int(math.sqrt(i))
                for j in [i-x**2 for x in range(m,0,-1)]:
                    ss.add(j)
            if 0 in ss:
                return index
            else:
                index += 1
                s = ss               
# @lc code=end

