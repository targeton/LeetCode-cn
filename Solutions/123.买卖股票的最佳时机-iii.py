#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (39.44%)
# Likes:    198
# Dislikes: 0
# Total Accepted:    11.5K
# Total Submissions: 29K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例 1:
# 
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
# 随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
# 
# 示例 2:
# 
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4
# 。   
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 
# 
# 示例 3:
# 
# 输入: [7,6,4,3,1] 
# 输出: 0 
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # general solution of dynamic programming:
        # state: dp[i][j][k], reprensents the maximum profit on holding k shares after j-th transaction on i-th day. k is assigned 0 or 1, have or not have stock
        # state transfer equation: dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+p[i]) and dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-p[i]). p is the price of stock
        # base case: dp[-1][j][0] = dp[i][0][0] = 0, dp[-1][j][1] = dp[i][0][1] = -infinity
        # we can optimize memory by space compression, just like the following solution:
        buy1,sell1,buy2,sell2 = float('-inf'), 0, float('-inf'),0
        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1+p)
            buy2 = max(buy2, sell1-p)
            sell2 = max(sell2, buy2+p)
        return sell2
# @lc code=end

