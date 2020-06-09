#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#
# https://leetcode-cn.com/problems/number-of-digit-one/description/
#
# algorithms
# Hard (36.10%)
# Likes:    130
# Dislikes: 0
# Total Accepted:    8K
# Total Submissions: 22.2K
# Testcase Example:  '13'
#
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
# 
# 示例:
# 
# 输入: 13
# 输出: 6 
# 解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
# 
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        dp, f = [0], 1
        tmp = n
        while tmp:
            dp.append(dp[-1]*10 + f)
            tmp //= 10
            f *= 10

        N = len(dp) - 1
        res = 0
        while N >= 0:
            base = 10**N
            m = n // base
            n = n % base
            if m == 1:
                res += n + 1 + dp[N]
            if m > 1:
                res += m * dp[N] + base
            N -= 1

        return res
        
# @lc code=end

