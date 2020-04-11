/*
 * @lc app=leetcode.cn id=154 lang=csharp
 *
 * [154] 寻找旋转排序数组中的最小值 II
 *
 * https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
 *
 * algorithms
 * Hard (44.45%)
 * Likes:    42
 * Dislikes: 0
 * Total Accepted:    5.7K
 * Total Submissions: 12.8K
 * Testcase Example:  '[1,3,5]'
 *
 * 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
 * 
 * ( 例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] )。
 * 
 * 请找出其中最小的元素。
 * 
 * 注意数组中可能存在重复的元素。
 * 
 * 示例 1：
 * 
 * 输入: [1,3,5]
 * 输出: 1
 * 
 * 示例 2：
 * 
 * 输入: [2,2,2,0,1]
 * 输出: 0
 * 
 * 说明：
 * 
 * 
 * 这道题是 寻找旋转排序数组中的最小值 的延伸题目。
 * 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
 * 
 * 
 */
public class Solution {
    public int FindMin(int[] nums) {
        int lo=0,hi=nums.Length-1;
        while(lo<hi){
            if(nums[lo]<nums[hi])
                return nums[lo];
            int mid = lo+(hi-lo)/2;
            if(nums[hi]>nums[mid]){
                hi=mid;
            }else if(nums[hi]<nums[mid]){
                lo=mid+1;
            }else{
                hi--;
            }
        }
        return nums[lo];
    }
}

