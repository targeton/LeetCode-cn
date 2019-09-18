/*
 * @lc app=leetcode.cn id=260 lang=csharp
 *
 * [260] 只出现一次的数字 III
 *
 * https://leetcode-cn.com/problems/single-number-iii/description/
 *
 * algorithms
 * Medium (66.54%)
 * Likes:    114
 * Dislikes: 0
 * Total Accepted:    8.7K
 * Total Submissions: 13K
 * Testcase Example:  '[1,2,1,3,2,5]'
 *
 * 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
 * 
 * 示例 :
 * 
 * 输入: [1,2,1,3,2,5]
 * 输出: [3,5]
 * 
 * 注意：
 * 
 * 
 * 结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
 * 你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
 * 
 * 
 */
public class Solution {
    public int[] SingleNumber(int[] nums) {
        int diff = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            diff ^= nums[i];
        }
        // get the lowest different bit of two single num
        diff &= -diff;
        int[] result = new int[2];
        for (int i = 0; i < nums.Length; i++)
        {
            if((nums[i] & diff) == 0)
                result[0] ^= nums[i];
            else
                result[1] ^= nums[i];
        }
        return result;
    }
}

