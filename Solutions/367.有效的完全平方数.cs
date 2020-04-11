/*
 * @lc app=leetcode.cn id=367 lang=csharp
 *
 * [367] 有效的完全平方数
 *
 * https://leetcode-cn.com/problems/valid-perfect-square/description/
 *
 * algorithms
 * Easy (41.44%)
 * Likes:    58
 * Dislikes: 0
 * Total Accepted:    12.2K
 * Total Submissions: 29.3K
 * Testcase Example:  '16'
 *
 * 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
 * 
 * 说明：不要使用任何内置的库函数，如  sqrt。
 * 
 * 示例 1：
 * 
 * 输入：16
 * 输出：True
 * 
 * 示例 2：
 * 
 * 输入：14
 * 输出：False
 * 
 * 
 */
public class Solution {
    public bool IsPerfectSquare(int num) {
        int lo = 1;
        int hi = num;
        while(lo <= hi){
            int mid = lo+(hi-lo)/2;
            if(num/mid==mid && num%mid==0){
                return true;
            }else if(num/mid > mid){
                lo = mid+1;
            }else{
                hi = mid-1;
            }
        }
        return false;
    }
}

