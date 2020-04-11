/*
 * @lc app=leetcode.cn id=32 lang=csharp
 *
 * [32] 最长有效括号
 *
 * https://leetcode-cn.com/problems/longest-valid-parentheses/description/
 *
 * algorithms
 * Hard (28.26%)
 * Likes:    327
 * Dislikes: 0
 * Total Accepted:    20.5K
 * Total Submissions: 72.6K
 * Testcase Example:  '"(()"'
 *
 * 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
 * 
 * 示例 1:
 * 
 * 输入: "(()"
 * 输出: 2
 * 解释: 最长有效括号子串为 "()"
 * 
 * 
 * 示例 2:
 * 
 * 输入: ")()())"
 * 输出: 4
 * 解释: 最长有效括号子串为 "()()"
 * 
 * 
 */
public class Solution {
    public int LongestValidParentheses(string s) {
        int max = 0;
        int[] dp = new int[s.Length];
        for (int i = 1; i < s.Length; i++)
        {
            if(s[i] == ')'){
                if(s[i-1] == '('){
                    dp[i] = (i-2) >= 0 ? dp[i-2]+2 : 2;
                    max = Math.Max(dp[i],max);
                }else{
                    if(i-dp[i-1]-1 >= 0 && s[i-dp[i-1]-1] == '('){
                        dp[i] = dp[i-1] + 2 + ((i-dp[i-1]-2 >= 0) ? dp[i-dp[i-1]-2] : 0);
                        max = Math.Max(dp[i],max);
                    }
                }
            }
        }
        return max;
    }
}

