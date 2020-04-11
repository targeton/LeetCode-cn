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
        int min = nums.Min(), max = nums.Max();
        // calculate gap of nums, if nums is evenly distributed then the calculated gap is max gap, else the max gap must lager than the calculated gap
        int bucketSize = Math.Max(1, (max - min) / (nums.Length - 1));
        List<int>[] buckets = new List<int>[(max - min) / bucketSize + 1];
        for(int i = 0; i < nums.Length; i++) {
            // determin bucket which nums[i] should be divided into 
            int pos = (nums[i] - min) / bucketSize;
            if(buckets[pos] == null) {
                buckets[pos] = new List<int>();
                // set bucket's min and max
                buckets[pos].Add(nums[i]);
                buckets[pos].Add(nums[i]);
            } else {
                // compare to bucket's min and max
                if (buckets[pos][0] > nums[i])
                    buckets[pos][0] = nums[i];
                if (buckets[pos][1] < nums[i])
                    buckets[pos][1] = nums[i];
            }            
        }
        // get max gap of buckets
        int prev = min, gap = 0;
        for (int i = 0; i < buckets.Length; i++) {
            if (buckets[i] == null)
                continue;
            if(buckets[i][0] - prev > gap)
                gap = buckets[i][0] - prev;
            prev = buckets[i][1];
        }
        return gap;
    }
}
// @lc code=end

