/*
 * @lc app=leetcode.cn id=152 lang=csharp
 *
 * [152] 乘积最大子序列
 *
 * https://leetcode-cn.com/problems/maximum-product-subarray/description/
 *
 * algorithms
 * Medium (35.43%)
 * Likes:    412
 * Dislikes: 0
 * Total Accepted:    38.7K
 * Total Submissions: 103.3K
 * Testcase Example:  '[2,3,-2,4]'
 *
 * 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
 * 
 * 示例 1:
 * 
 * 输入: [2,3,-2,4]
 * 输出: 6
 * 解释: 子数组 [2,3] 有最大乘积 6。
 * 
 * 
 * 示例 2:
 * 
 * 输入: [-2,0,-1]
 * 输出: 0
 * 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
 * 
 */

// @lc code=start
public class Solution {
    public int MaxProduct(int[] nums) {
        int[,] dp = new int[2,2];
        int max = nums[0];
        dp[0,0] = max;
        for(int i = 1; i < nums.Length; i++){
            int p = i % 2, q = (i - 1) % 2;
            dp[p,0] = Math.Max(Math.Max(dp[q,0]*nums[i], dp[q,1]*nums[i]), nums[i]);
            dp[p,1] = Math.Min(Math.Min(dp[q,0]*nums[i],dp[q,1]*nums[i]), nums[i]);
            max = Math.Max(max,dp[p,0]);
        }
        return max;
    }
}
// @lc code=end

