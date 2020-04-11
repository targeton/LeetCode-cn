/*
 * @lc app=leetcode.cn id=313 lang=csharp
 *
 * [313] 超级丑数
 *
 * https://leetcode-cn.com/problems/super-ugly-number/description/
 *
 * algorithms
 * Medium (57.21%)
 * Likes:    56
 * Dislikes: 0
 * Total Accepted:    4.9K
 * Total Submissions: 8.1K
 * Testcase Example:  '12\n[2,7,13,19]'
 *
 * 编写一段程序来查找第 n 个超级丑数。
 * 
 * 超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。
 * 
 * 示例:
 * 
 * 输入: n = 12, primes = [2,7,13,19]
 * 输出: 32 
 * 解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12
 * 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
 * 
 * 说明:
 * 
 * 
 * 1 是任何给定 primes 的超级丑数。
 * 给定 primes 中的数字以升序排列。
 * 0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000 。
 * 第 n 个超级丑数确保在 32 位有符整数范围内。
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int NthSuperUglyNumber(int n, int[] primes) {
        int[] dp = new int[n];
        int[] indexs = new int[primes.Length];
        int[] vals = new int[primes.Length];
        int next = 1;
        for (int i = 0; i < n; i++)
        {
            dp[i] = next;
            next = int.MaxValue;
            for(int j = 0; j < primes.Length; j++){
                if(vals[j] <= dp[i]){
                    vals[j] = dp[indexs[j]++] * primes[j];
                }
                next = Math.Min(vals[j], next);
            }
        }
        return dp[n-1];
    }
}
// @lc code=end

