/*
 * @lc app=leetcode.cn id=647 lang=csharp
 *
 * [647] 回文子串
 *
 * https://leetcode-cn.com/problems/palindromic-substrings/description/
 *
 * algorithms
 * Medium (57.21%)
 * Likes:    127
 * Dislikes: 0
 * Total Accepted:    8K
 * Total Submissions: 13.9K
 * Testcase Example:  '"abc"'
 *
 * 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
 * 
 * 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
 * 
 * 示例 1:
 * 
 * 
 * 输入: "abc"
 * 输出: 3
 * 解释: 三个回文子串: "a", "b", "c".
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: "aaa"
 * 输出: 6
 * 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
 * 
 * 
 * 注意:
 * 
 * 
 * 输入的字符串长度不会超过1000。
 * 
 * 
 */
public class Solution {
    int count = 0;
    public int CountSubstrings(string s) {
        if(string.IsNullOrEmpty(s))
            return 0;
        for(int i=0;i<s.Length;i++){
            Extend(s,i,i);
            Extend(s,i,i+1);
        }
        return count;
    }
    private void Extend(string s,int left,int right){
        while(left >= 0 && right < s.Length && s[left] == s[right]){
            count++;
            left--;
            right++;
        }
    }
}

