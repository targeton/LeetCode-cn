/*
 * @lc app=leetcode.cn id=7 lang=csharp
 *
 * [7] 整数反转
 *
 * https://leetcode-cn.com/problems/reverse-integer/description/
 *
 * algorithms
 * Easy (33.86%)
 * Likes:    1760
 * Dislikes: 0
 * Total Accepted:    305.3K
 * Total Submissions: 901.3K
 * Testcase Example:  '123'
 *
 * 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
 * 
 * 示例 1:
 * 
 * 输入: 123
 * 输出: 321
 * 
 * 
 * 示例 2:
 * 
 * 输入: -123
 * 输出: -321
 * 
 * 
 * 示例 3:
 * 
 * 输入: 120
 * 输出: 21
 * 
 * 
 * 注意:
 * 
 * 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回
 * 0。
 * 
 */

// @lc code=start
public class Solution {
    public int Reverse(int x) {
        bool flag = x < 0 ? true : false;
        int result = 0;
        while (x != 0)
        {
            int r = x % 10;
            x = x / 10;
            if (result > int.MaxValue / 10 || (result == int.MaxValue / 10 && r > int.MaxValue % 10)) {
                result = 0;
                break;
            } else if (result < int.MinValue / 10 || (result == int.MinValue / 10 && r < int.MinValue % 10)) {
                result = 0;
                break;
            }
            result = 10 * result + r;
        }
        return result;
    }
}
// @lc code=end

