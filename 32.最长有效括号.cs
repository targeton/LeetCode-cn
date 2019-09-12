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
        Stack<int> stack = new Stack<int>();
        for (int i = 0; i < s.Length; i++)
        {
            if(s[i] == '('){
                stack.Push(i);
            }else{
                if(stack.Count() > 0 && s[stack.Peek()] == '('){
                    stack.Pop();
                }else{
                    stack.Push(i);
                }
            }
        }
        int b = s.Length;
        int a = 0;
        int max = 0;
        while(stack.Count()>0){
            a = stack.Pop();
            if(b-a > max)
                max = b-a-1;
            b = a;
        }
        if(b> max)
            max = b;
        return max;
    }
}

