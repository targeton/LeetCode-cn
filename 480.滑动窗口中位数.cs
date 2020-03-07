/*
 * @lc app=leetcode.cn id=480 lang=csharp
 *
 * [480] 滑动窗口中位数
 *
 * https://leetcode-cn.com/problems/sliding-window-median/description/
 *
 * algorithms
 * Hard (30.29%)
 * Likes:    50
 * Dislikes: 0
 * Total Accepted:    2.7K
 * Total Submissions: 8K
 * Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
 *
 * 中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。
 * 
 * 例如：
 * 
 * [2,3,4]，中位数是 3
 * 
 * [2,3]，中位数是 (2 + 3) / 2 = 2.5
 * 
 * 给出一个数组 nums，有一个大小为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1
 * 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。
 * 
 * 
 * 
 * 示例：
 * 
 * 给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。
 * 
 * 窗口位置                      中位数
 * ---------------               -----
 * [1  3  -1] -3  5  3  6  7       1
 * ⁠1 [3  -1  -3] 5  3  6  7       -1
 * ⁠1  3 [-1  -3  5] 3  6  7       -1
 * ⁠1  3  -1 [-3  5  3] 6  7       3
 * ⁠1  3  -1  -3 [5  3  6] 7       5
 * ⁠1  3  -1  -3  5 [3  6  7]      6
 * 
 * 
 * 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。
 * 与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。
 * 
 * 
 */

// @lc code=start
public class Solution {
    public double[] MedianSlidingWindow(int[] nums, int k) {
        if(nums == null)
            return new double[0];
        double[] result = new double[nums.Length-k+1];
        List<int> window = nums.Take(k).OrderBy(n => n).ToList();
        result[0] = GetMiddle(window, k);
        for (int i = k; i < nums.Length; i++)
        {
            var r = FindRemoveIndex(window, nums[i-k]);
            window.RemoveAt(r);
            var pos = FindInsertIndex(window, nums[i]);
            window.Insert(pos,nums[i]);
            result[i-k+1] = GetMiddle(window, k);
        }
        return result;
    }

    private int FindRemoveIndex(List<int> nums, int target){
        int p = 0, q = nums.Count() - 1;
        while(p < q){
            int mid = (p + q) / 2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] > target)
                q = mid - 1;
            else
                p = mid + 1;
        }
        return p;
    }

    private int FindInsertIndex(List<int> nums, int target){
        int p = 0, q = nums.Count();
        while (p < q)
        {
            int mid = (p + q) / 2;
            if(nums[mid] < target)
                p = mid + 1;
            else
                q = mid;
        }
        return p;
    }

    private double GetMiddle(List<int> nums, int length){
        if(length % 2 == 1){
            return nums[length/2] * 1.0;
        }else{
            return nums[length/2-1] * 1.0 / 2 + nums[length/2] * 1.0 / 2.0;
        }
    }
}
// @lc code=end

