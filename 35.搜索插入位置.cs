/*
 * @lc app=leetcode.cn id=35 lang=csharp
 *
 * [35] 搜索插入位置
 *
 * https://leetcode-cn.com/problems/search-insert-position/description/
 *
 * algorithms
 * Easy (44.31%)
 * Likes:    429
 * Dislikes: 0
 * Total Accepted:    115.5K
 * Total Submissions: 256.2K
 * Testcase Example:  '[1,3,5,6]\n5'
 *
 * 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
 * 
 * 你可以假设数组中无重复元素。
 * 
 * 示例 1:
 * 
 * 输入: [1,3,5,6], 5
 * 输出: 2
 * 
 * 
 * 示例 2:
 * 
 * 输入: [1,3,5,6], 2
 * 输出: 1
 * 
 * 
 * 示例 3:
 * 
 * 输入: [1,3,5,6], 7
 * 输出: 4
 * 
 * 
 * 示例 4:
 * 
 * 输入: [1,3,5,6], 0
 * 输出: 0
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int SearchInsert(int[] nums, int target) {
        int p = 0, q = nums.Length;
        while(p < q){
            var mid  = (p + q) / 2;
            if(nums[mid] < target)
                p = mid + 1;
            else if(nums[mid] == target)
                return mid;
            else
                q = mid;
        }
        return p;
    }
}
// @lc code=end

