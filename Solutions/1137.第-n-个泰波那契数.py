#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#
# https://leetcode-cn.com/problems/n-th-tribonacci-number/description/
#
# algorithms
# Easy (52.21%)
# Likes:    30
# Dislikes: 0
# Total Accepted:    11.5K
# Total Submissions: 22.1K
# Testcase Example:  '4'
#
# 泰波那契序列 Tn 定义如下： 
# 
# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
# 
# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 4
# 输出：4
# 解释：
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# 
# 
# 示例 2：
# 
# 输入：n = 25
# 输出：1389537
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 37
# 答案保证是一个 32 位整数，即 answer <= 2^31 - 1。
# 
# 
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        dp_0, dp_1, dp_2 = 0, 0, 1
        res = 0
        while n > 1:
            res = dp_0 + dp_1 + dp_2
            dp_0, dp_1, dp_2 = dp_1, dp_2, res
            n -= 1
        return res 
# @lc code=end

