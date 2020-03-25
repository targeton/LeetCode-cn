/*
 * @lc app=leetcode.cn id=164 lang=csharp
 *
 * [164] 最大间距
 *
 * https://leetcode-cn.com/problems/maximum-gap/description/
 *
 * algorithms
 * Hard (54.60%)
 * Likes:    123
 * Dislikes: 0
 * Total Accepted:    12.1K
 * Total Submissions: 22.2K
 * Testcase Example:  '[3,6,9,1]'
 *
 * 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
 * 
 * 如果数组元素个数小于 2，则返回 0。
 * 
 * 示例 1:
 * 
 * 输入: [3,6,9,1]
 * 输出: 3
 * 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
 * 
 * 示例 2:
 * 
 * 输入: [10]
 * 输出: 0
 * 解释: 数组元素个数小于 2，因此返回 0。
 * 
 * 说明:
 * 
 * 
 * 你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
 * 请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int MaximumGap(int[] nums) {
        if(nums == null || nums.Length < 2)
            return 0;
        int divide = 1;
        int max = nums.Max();
        while (max / divide > 0) {
            List<int>[] cache = new List<int>[10];
            for (int i = 0; i < nums.Length; i++) {
                int pos = nums[i] / divide % 10;
                if (cache[pos] == null) 
                    cache[pos] = new List<int>();
                cache[pos].Add(nums[i]);
            }
            int index = 0;
            for (int i = 0; i < 10; i++) {
                if (cache[i] == null)
                    continue;
                for (int j = 0; j < cache[i].Count(); j++) {
                    nums[index++] = cache[i][j];
                }
            }
            divide *= 10;
        }
        int gap = 0;
        for (int i = 0; i < nums.Length - 1; i++) {
            if (nums[i+1] - nums[i] > gap)
                gap = nums[i+1] - nums[i];
        }
        return gap;
    }
}
// @lc code=end

