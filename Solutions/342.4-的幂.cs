/*
 * @lc app=leetcode.cn id=342 lang=csharp
 *
 * [342] 4的幂
 *
 * https://leetcode-cn.com/problems/power-of-four/description/
 *
 * algorithms
 * Easy (46.66%)
 * Likes:    80
 * Dislikes: 0
 * Total Accepted:    18K
 * Total Submissions: 38K
 * Testcase Example:  '16'
 *
 * 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
 * 
 * 示例 1:
 * 
 * 输入: 16
 * 输出: true
 * 
 * 
 * 示例 2:
 * 
 * 输入: 5
 * 输出: false
 * 
 * 进阶：
 * 你能不使用循环或者递归来完成本题吗？
 * 
 */

// @lc code=start
public class Solution {
    public bool IsPowerOfFour(int num) {
        // 需满足条件：bit位有且只有一个1，且1位于奇数位
        return ((num - 1) & num) == 0 && (num & 0x55555555) != 0;
    }
}
// @lc code=end

