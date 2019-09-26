/*
 * @lc app=leetcode.cn id=188 lang=csharp
 *
 * [188] 买卖股票的最佳时机 IV
 *
 * https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/
 *
 * algorithms
 * Hard (27.59%)
 * Likes:    115
 * Dislikes: 0
 * Total Accepted:    6.1K
 * Total Submissions: 22K
 * Testcase Example:  '2\n[2,4,1]'
 *
 * 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
 * 
 * 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
 * 
 * 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
 * 
 * 示例 1:
 * 
 * 输入: [2,4,1], k = 2
 * 输出: 2
 * 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
 * 
 * 
 * 示例 2:
 * 
 * 输入: [3,2,6,5,0,3], k = 2
 * 输出: 7
 * 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4
 * 。
 * 随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
 * 
 * 
 */
public class Solution {
    public int MaxProfit(int k, int[] prices) {
        int p = prices.Length;
        int profit = 0;
        if(k >= p/2){
            for (int i = 1; i < p; i++)
            {
                profit += Math.Max(0, prices[i]-prices[i-1]);
            }
            return profit;
        }
        var dp = new int[k+1,p];
        for (int i = 1; i <= k; i++)
        {
            var minBuy = prices[0];
            for (int j = 1; j < p; j++)
            {
                minBuy = Math.Min(minBuy, prices[j] - dp[i-1, j-1]);
                dp[i,j] = Math.Max(dp[i,j-1], prices[j] - minBuy);
            }
        }
        return dp[k,p-1];
    }
}

