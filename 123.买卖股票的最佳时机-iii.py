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
        # if not prices: return 0
        # maxint = 2**32-1

        # profit = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]

        # profit[0][0][0], profit[0][0][1] = 0, -prices[0]
        # profit[0][1][0], profit[0][1][1] = -maxint, -maxint
        # profit[0][2][0], profit[0][2][1] = -maxint, -maxint

        # for i in range(1, len(prices)):
        #     profit[i][0][0] = profit[i-1][0][0]
        #     profit[i][0][1] = max(profit[i-1][0][1], profit[i-1][0][0]-prices[i])

        #     profit[i][1][0] = max(profit[i-1][1][0], profit[i-1][0][1]+prices[i])
        #     profit[i][1][1] = max(profit[i-1][1][1], profit[i-1][1][0]-prices[i])

        #     profit[i][2][0] = max(profit[i-1][2][0], profit[i-1][1][1]+prices[i])
        
        # d=len(prices)-1
        # return max(profit[d][0][0], profit[d][1][0], profit[d][2][0])
        buy1,sell1,buy2,sell2 = 2**32-1,0,2**32-1,0
        for p in prices:
            buy1 = min(buy1, p)
            sell1 = max(sell1, p-buy1)
            buy2 = min(buy2, p-sell1)
            sell2 = max(sell2, p-buy2)
        return sell2
# @lc code=end

