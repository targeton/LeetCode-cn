/*
 * @lc app=leetcode.cn id=410 lang=csharp
 *
 * [410] 分割数组的最大值
 *
 * https://leetcode-cn.com/problems/split-array-largest-sum/description/
 *
 * algorithms
 * Hard (37.39%)
 * Likes:    48
 * Dislikes: 0
 * Total Accepted:    1.7K
 * Total Submissions: 4.5K
 * Testcase Example:  '[7,2,5,10,8]\n2'
 *
 * 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
 * 
 * 注意:
 * 数组长度 n 满足以下条件:
 * 
 * 
 * 1 ≤ n ≤ 1000
 * 1 ≤ m ≤ min(50, n)
 * 
 * 
 * 示例: 
 * 
 * 
 * 输入:
 * nums = [7,2,5,10,8]
 * m = 2
 * 
 * 输出:
 * 18
 * 
 * 解释:
 * 一共有四种方法将nums分割为2个子数组。
 * 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
 * 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
 * 
 * 
 */
public class Solution {
    public int SplitArray(int[] nums, int m) {
        int L = nums.Length;
        int[] S = new int[L+1];
        S[0] = 0;
        for (int i = 0; i < L; i++)
        {
            S[i+1] = S[i]+nums[i];
        }
        int[] dp = new int[L];
        for(int i = 0; i<L; i++)
            dp[i] = S[L] - S[i];
        for (int s = 1; s < m; s++)
        {
            for (int i = 0; i < L-s; i++)
            {
                dp[i] = Int32.MaxValue;
                for(int j = i+1; j <= L-s; j++){
                    int t = Math.Max(dp[j],S[j]-S[i]);
                    if(t < dp[i])
                        dp[i] = t;
                }
            }
        }
        return dp[0];
    }
}

