/*
 * @lc app=leetcode.cn id=67 lang=csharp
 *
 * [67] 二进制求和
 *
 * https://leetcode-cn.com/problems/add-binary/description/
 *
 * algorithms
 * Easy (50.61%)
 * Likes:    301
 * Dislikes: 0
 * Total Accepted:    61.9K
 * Total Submissions: 118.7K
 * Testcase Example:  '"11"\n"1"'
 *
 * 给定两个二进制字符串，返回他们的和（用二进制表示）。
 * 
 * 输入为非空字符串且只包含数字 1 和 0。
 * 
 * 示例 1:
 * 
 * 输入: a = "11", b = "1"
 * 输出: "100"
 * 
 * 示例 2:
 * 
 * 输入: a = "1010", b = "1011"
 * 输出: "10101"
 * 
 */

// @lc code=start
public class Solution {
    public string AddBinary(string a, string b) {
        var sb = new StringBuilder();
        int carry = 0;
        int i = a.Length - 1, j = b.Length - 1;
        while(i >= 0 || j >= 0){
            int sum = carry;
            if(i >= 0)
                sum += a[i--] - '0';
            if(j >= 0)
                sum += b[j--] - '0';
            sb.Insert(0, sum % 2);
            carry = sum / 2;
        }
        if(carry == 1)
            sb.Insert(0, 1);
        return sb.ToString();        
    }
}
// @lc code=end

