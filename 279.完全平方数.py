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
        # dynamic programming: numSquares(n) = min(numSquares(n-k)+1) k∈square_num
        square_num = [x**2 for x in range(0, int(n**0.5) + 1)]
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for square in square_num:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square]+1)
        return dp[-1]
# @lc code=end

