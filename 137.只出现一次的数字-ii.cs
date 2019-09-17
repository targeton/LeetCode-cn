/*
 * @lc app=leetcode.cn id=137 lang=csharp
 *
 * [137] 只出现一次的数字 II
 *
 * https://leetcode-cn.com/problems/single-number-ii/description/
 *
 * algorithms
 * Medium (64.40%)
 * Likes:    183
 * Dislikes: 0
 * Total Accepted:    12.8K
 * Total Submissions: 19.8K
 * Testcase Example:  '[2,2,3,2]'
 *
 * 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
 * 
 * 说明：
 * 
 * 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
 * 
 * 示例 1:
 * 
 * 输入: [2,2,3,2]
 * 输出: 3
 * 
 * 
 * 示例 2:
 * 
 * 输入: [0,1,0,1,0,1,99]
 * 输出: 99
 * 
 */
public class Solution {
    public int SingleNumber(int[] nums) {
        int ans = 0;
        for (int i = 0; i < 32; i++)
        {
            int sum = 0;
            for (int j = 0; j < nums.Length; j++)
            {
                if(((nums[j]>>i) & 1) == 1){
                    sum++;
                    sum %= 3;
                }
            }
            if(sum != 0){
                ans |= sum << i;
            }
        }
        return ans;
    }
}

