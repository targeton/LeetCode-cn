#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#
# https://leetcode-cn.com/problems/sum-of-two-integers/description/
#
# algorithms
# Medium (58.05%)
# Likes:    484
# Dislikes: 0
# Total Accepted:    64.1K
# Total Submissions: 107.3K
# Testcase Example:  '1\n2'
#
# 给你两个整数 a 和 b ，不使用 运算符 + 和 - ​​​​​​​，计算并返回两整数之和。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：a = 1, b = 2
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：a = 2, b = 3
# 输出：5
# 
# 
# 
# 
# 提示：
# 
# 
# -1000 <= a, b <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK= 0xFFFFFFFF
        a = a & MASK
        b = b & MASK
        while b != 0:
            carry = ((a & b) << 1) & MASK
            a = a ^ b
            b = carry
        return a if a < 0x80000000 else ~(a ^ MASK)
# @lc code=end

