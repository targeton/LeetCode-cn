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
        # greedy + recursive, condition setting of greedy is: n can be divided by count, count from 1,2,...
        squares_num = [x**2 for x in range(0, int(n**0.5)+1)]
        def isDivided(n, count):
            if count == 1:
                return n in squares_num
            for k in squares_num:
                if isDivided(n-k,count-1):
                    return True
            return False
        
        for count in range(1, n+1):
            if isDivided(n,count):
                return count
# @lc code=end

