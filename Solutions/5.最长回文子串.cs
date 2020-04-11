/*
 * @lc app=leetcode.cn id=5 lang=csharp
 *
 * [5] 最长回文子串
 *
 * https://leetcode-cn.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (27.14%)
 * Likes:    1839
 * Dislikes: 0
 * Total Accepted:    200.8K
 * Total Submissions: 696.4K
 * Testcase Example:  '"babad"'
 *
 * 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
 * 
 * 示例 1：
 * 
 * 输入: "babad"
 * 输出: "bab"
 * 注意: "aba" 也是一个有效答案。
 * 
 * 
 * 示例 2：
 * 
 * 输入: "cbbd"
 * 输出: "bb"
 * 
 * 
 */

// @lc code=start
public class Solution {
    public string LongestPalindrome(string s) {
        if(string.IsNullOrEmpty(s))
            return "";
        int max = 0, p = 0, q = 0, pos = 0;
        for(int i = 0; i < s.Length; i++){
            int tmp1 = 1;
            p = i - 1;
            q = i + 1;            
            while(p >= 0 && q < s.Length && s[p] == s[q]){
                tmp1 += 2;
                p--;
                q++;
            }
            int tmp2 = 0;
            if(i+1<s.Length && s[i] == s[i+1]){
                p = i-1;
                q = i+2;
                tmp2 += 2;
                while(p >= 0 && q < s.Length && s[p] == s[q]){
                    tmp2 += 2;
                    p--;
                    q++;
                }
            }
            var tmp = tmp1 >= tmp2 ? tmp1 : tmp2;
            if(max < tmp){
                max = tmp;
                pos = i;
            }
        }
        pos = max % 2 == 0 ? pos - max / 2 + 1 : pos - max / 2; 
        return s.Substring(pos, max);
    }
}
// @lc code=end

