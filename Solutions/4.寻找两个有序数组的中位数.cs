/*
 * @lc app=leetcode.cn id=4 lang=csharp
 *
 * [4] 寻找两个有序数组的中位数
 *
 * https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (35.61%)
 * Likes:    1323
 * Dislikes: 0
 * Total Accepted:    74.1K
 * Total Submissions: 207.8K
 * Testcase Example:  '[1,3]\n[2]'
 *
 * 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
 * 
 * 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
 * 
 * 你可以假设 nums1 和 nums2 不会同时为空。
 * 
 * 示例 1:
 * 
 * nums1 = [1, 3]
 * nums2 = [2]
 * 
 * 则中位数是 2.0
 * 
 * 
 * 示例 2:
 * 
 * nums1 = [1, 2]
 * nums2 = [3, 4]
 * 
 * 则中位数是 (2 + 3)/2 = 2.5
 * 
 * 
 */
public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.Length, n = nums2.Length;
        return (FindKthSmallestNum(nums1, 0, m-1, nums2, 0, n-1, (m+n+1)/2) + FindKthSmallestNum(nums1, 0, m-1, nums2, 0, n-1, (m+n+2)/2))/2.0;
    }

    private int FindKthSmallestNum(int[] nums1, int start1, int end1, int[] nums2, int start2, int end2, int k) {
    	int len1 = end1 - start1 + 1;
    	int len2 = end2 - start2 + 1;
    	if (len1 > len2) return FindKthSmallestNum(nums2, start2, end2, nums1, start1, end1, k);
    	if (len1 == 0) return nums2[start2 + k - 1];
    	if (k == 1) return Math.Min(nums1[start1], nums2[start2]);
    	
    	int i = start1 + Math.Min(len1, k / 2) - 1;
    	int j = start2 + Math.Min(len2, k / 2) - 1;
    	//Eliminate half of the elements from one of the smaller arrays
    	if (nums1[i] > nums2[j]) {
    		return FindKthSmallestNum(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1));
    	}
    	else {
    		return FindKthSmallestNum(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1));
    	}
    }
}

