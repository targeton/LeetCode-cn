/*
 * @lc app=leetcode.cn id=303 lang=csharp
 *
 * [303] 区域和检索 - 数组不可变
 *
 * https://leetcode-cn.com/problems/range-sum-query-immutable/description/
 *
 * algorithms
 * Easy (55.70%)
 * Likes:    95
 * Dislikes: 0
 * Total Accepted:    16K
 * Total Submissions: 28.6K
 * Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
 *
 * 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
 * 
 * 示例：
 * 
 * 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
 * 
 * sumRange(0, 2) -> 1
 * sumRange(2, 5) -> -1
 * sumRange(0, 5) -> -3
 * 
 * 说明:
 * 
 * 
 * 你可以假设数组不可变。
 * 会多次调用 sumRange 方法。
 * 
 * 
 */
public class NumArray {

    private int[] _sum;
    
    public NumArray(int[] nums) {
        _sum = new int[nums.Length];
        int tmp = 0;
        for(int i = 0; i < nums.Length; i++){
            tmp += nums[i];
            _sum[i] = tmp;
        }
    }
    
    public int SumRange(int i, int j) {
        int lower = i-1<0 ? 0 : _sum[i-1];
        return _sum[j] - lower;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.SumRange(i,j);
 */

