#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#
# https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/description/
#
# algorithms
# Easy (44.19%)
# Likes:    74
# Dislikes: 0
# Total Accepted:    21.5K
# Total Submissions: 48.2K
# Testcase Example:  '[1,3,5,4,7]'
#
# 给定一个未经排序的整数数组，找到最长且连续的的递增序列。
# 
# 示例 1:
# 
# 
# 输入: [1,3,5,4,7]
# 输出: 3
# 解释: 最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。 
# 
# 
# 示例 2:
# 
# 
# 输入: [2,2,2,2,2]
# 输出: 1
# 解释: 最长连续递增序列是 [2], 长度为1。
# 
# 
# 注意：数组长度不会超过10000。
# 
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res, i, j = 1, 0, 1
        while j < len(nums):
            if nums[j] <= nums[j-1]:
                res = max(res,j-i)
                i = j
            j += 1
        res = max(res, j-i)
        return res
# @lc code=end

