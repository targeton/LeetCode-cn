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
        for (int i = 2; i < n; i++)
        {
            if(notPrimes[i] == false)
                count++;
            if(i > n / i)
                continue;
            for (int j = i * i; j < n; j = j + i)
            {
                notPrimes[j] = true;
            }
        }
        return count;
    }
}
// @lc code=end

