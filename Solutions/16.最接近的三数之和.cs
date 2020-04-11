/*
 * @lc app=leetcode.cn id=16 lang=csharp
 *
 * [16] 最接近的三数之和
 *
 * https://leetcode-cn.com/problems/3sum-closest/description/
 *
 * algorithms
 * Medium (41.67%)
 * Likes:    365
 * Dislikes: 0
 * Total Accepted:    74.3K
 * Total Submissions: 172.8K
 * Testcase Example:  '[-1,2,1,-4]\n1'
 *
 * 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
 * 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
 * 
 * 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
 * 
 * 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int ThreeSumClosest(int[] nums, int target) {
        QuickSort(nums, 0, nums.Length-1);
        var result = nums[0] + nums[1] + nums[2];
        if(result >= target)
            return result;
        for (int i = 0; i < nums.Length; i++)
        {
            int p = i + 1;
            int q = nums.Length - 1;            
            while(p < q) {
                var sum = nums[i] + nums[p] + nums[q];
                if(Math.Abs(sum - target) < Math.Abs(result - target))
                    result = sum;
                if(sum == target)
                    return target;
                if(sum > target)
                    q--;
                else
                    p++;
            }
        }   
        return result;     
    }

    private void QuickSort(int[] nums, int left, int right) {
        if(left >= right)
            return;
        var tmp = nums[left];
        int i = left;
        for (int j = left + 1; j <= right; j++)
        {
            if(nums[j] < tmp){
                nums[i] = nums[j];
                nums[j] = nums[i+1];
                i++;
            }
        }
        nums[i] = tmp;
        QuickSort(nums, left, i - 1);
        QuickSort(nums, i + 1, right);
    }
}
// @lc code=end

