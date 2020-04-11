/*
 * @lc app=leetcode.cn id=300 lang=csharp
 *
 * [300] 最长上升子序列
 *
 * https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
 *
 * algorithms
 * Medium (43.91%)
 * Likes:    568
 * Dislikes: 0
 * Total Accepted:    77.1K
 * Total Submissions: 175.5K
 * Testcase Example:  '[10,9,2,5,3,7,101,18]'
 *
 * 给定一个无序的整数数组，找到其中最长上升子序列的长度。
 * 
 * 示例:
 * 
 * 输入: [10,9,2,5,3,7,101,18]
 * 输出: 4 
 * 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
 * 
 * 说明:
 * 
 * 
 * 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
 * 你算法的时间复杂度应该为 O(n^2) 。
 * 
 * 
 * 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
 * 
 */

// @lc code=start
public class Solution {
    public int LengthOfLIS(int[] nums) {
        if(nums == null || nums.Length == 0)
            return 0;        
        List<int> list = new List<int>(){nums[0]};
        for(int i = 1; i < nums.Length; i++) {
            if(nums[i] > list[list.Count() - 1]) {
                list.Add(nums[i]);
            } else {
                var pos = FindPos(list, nums[i]);
                list[pos] = nums[i];
            }
        }
        return list.Count();
    }

    private int FindPos(List<int> list, int target) {
        int p = -1, q = list.Count() - 1;
        while(p < q) {
            int mid = (p + q + 1) / 2;
            if(list[mid] < target) {
                p = mid;
            } else {
                q = mid - 1;
            }
        }
        return p + 1;
    }
}
// @lc code=end

