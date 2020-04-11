#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (52.48%)
# Likes:    253
# Dislikes: 0
# Total Accepted:    19.2K
# Total Submissions: 36.3K
# Testcase Example:  '[1,2,3,0,2]'
#
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
# 
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 
# 
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 
# 
# 示例:
# 
# 输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # refer to solution for No.123 problem
        # dp[i,0] = max(dp[i-1,0], dp[i-1,1]+p[i])
        # dp[i,1] = max(dp[i-1,1], dp[i-2,0]-p[i])
        dp_prev, dp_0, dp_1 = 0, 0, float('-inf')
        for p in prices:
            tmp = dp_0
            dp_0 = max(dp_0, dp_1 + p)
            dp_1 = max(dp_1, dp_prev - p)
            dp_prev = tmp
        return dp_0
# @lc code=end

