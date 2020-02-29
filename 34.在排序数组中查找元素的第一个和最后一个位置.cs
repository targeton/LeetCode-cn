/*
 * @lc app=leetcode.cn id=34 lang=csharp
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 *
 * https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
 *
 * algorithms
 * Medium (37.72%)
 * Likes:    329
 * Dislikes: 0
 * Total Accepted:    66.4K
 * Total Submissions: 169.9K
 * Testcase Example:  '[5,7,7,8,8,10]\n8'
 *
 * 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
 * 
 * 你的算法时间复杂度必须是 O(log n) 级别。
 * 
 * 如果数组中不存在目标值，返回 [-1, -1]。
 * 
 * 示例 1:
 * 
 * 输入: nums = [5,7,7,8,8,10], target = 8
 * 输出: [3,4]
 * 
 * 示例 2:
 * 
 * 输入: nums = [5,7,7,8,8,10], target = 6
 * 输出: [-1,-1]
 * 
 */

// @lc code=start
public class Solution {
    public int[] SearchRange(int[] nums, int target) {
        if(nums == null || nums.Length == 0)
            return new int[]{-1,-1};
        int[] result = new int[2];
        result[0] = FindLeft(nums,target);
        result[1] = FindRight(nums,target);
        return result;
    }

    private int FindLeft(int[] nums, int target){
        int p = 0, q = nums.Length;
        while (p < q)
        {
            int mid = (p + q) / 2;
            if(nums[mid] >= target)
                q = mid;
            else
                p = mid + 1;
        }
        return p == nums.Length ? -1 : (nums[p] == target ? p : -1);
    }
    
    private int FindRight(int[] nums, int target){
        int p = -1, q = nums.Length - 1;
        while (p < q)
        {
            int mid = (p + q + 1) / 2;
            if(nums[mid] <= target)
                p = mid;
            else
                q = mid - 1;
        }
        return p == -1 ? -1 : (nums[p] == target ? p : -1);
    }
}
// @lc code=end

