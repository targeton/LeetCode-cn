/*
 * @lc app=leetcode.cn id=204 lang=csharp
 *
 * [204] 计数质数
 *
 * https://leetcode-cn.com/problems/count-primes/description/
 *
 * algorithms
 * Easy (30.08%)
 * Likes:    262
 * Dislikes: 0
 * Total Accepted:    39.7K
 * Total Submissions: 124.7K
 * Testcase Example:  '10'
 *
 * 统计所有小于非负整数 n 的质数的数量。
 * 
 * 示例:
 * 
 * 输入: 10
 * 输出: 4
 * 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int CountPrimes(int n) {
        bool[] notPrimes = new bool[n];
        int count = 0;
        int pos = (int)Math.Sqrt(n) + 1;
        for (int i = 2; i < pos; i++)
        {
            if(notPrimes[i] == false)
            {
                count++;
                for(int j=2; i * j < n; j++)
                {
                    notPrimes[i*j] = true;
                }
            }            
        }
        for (int i = pos; i < n; i++)
        {
            if(notPrimes[i] == false)
                count++;
        }
        return count;
    }
}
// @lc code=end

