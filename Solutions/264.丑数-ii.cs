/*
 * @lc app=leetcode.cn id=264 lang=csharp
 *
 * [264] 丑数 II
 *
 * https://leetcode-cn.com/problems/ugly-number-ii/description/
 *
 * algorithms
 * Medium (47.60%)
 * Likes:    201
 * Dislikes: 0
 * Total Accepted:    15.2K
 * Total Submissions: 31.1K
 * Testcase Example:  '10'
 *
 * 编写一个程序，找出第 n 个丑数。
 * 
 * 丑数就是只包含质因数 2, 3, 5 的正整数。
 * 
 * 示例:
 * 
 * 输入: n = 10
 * 输出: 12
 * 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
 * 
 * 说明:  
 * 
 * 
 * 1 是丑数。
 * n 不超过1690。
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int NthUglyNumber(int n) {
        int[] dp = new int[n];
        dp[0] = 1;
        int twoIndex = 0, threeIndex = 0, fiveIndex = 0;
        for(int i = 1; i < n; i++){
            var two = dp[twoIndex] * 2;
            var three = dp[threeIndex] * 3;
            var five = dp[fiveIndex] * 5;
            var min = Math.Min(two, Math.Min(three, five));
            if(min == two){
                twoIndex++;
            }
            if(min == three){
                threeIndex++;
            }
            if(min == five){
                fiveIndex++;
            }
            dp[i] = min;
        }
        return dp[n-1];
    }
}
// @lc code=end

