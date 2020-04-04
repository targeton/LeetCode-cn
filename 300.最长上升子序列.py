#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (43.91%)
# Likes:    568
# Dislikes: 0
# Total Accepted:    77.1K
# Total Submissions: 175.5K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
# 
# 示例:
# 
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 
# 说明:
# 
# 
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
# 
# 
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
# 
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        # dp[j] = max(dp[i])+1 which nums[i] < nums[j] and i < j
        for i in range(len(nums)):
            tmp = []
            for j in range(i):
                if nums[j] < nums[i]:
                    tmp.append(dp[j])
            if(len(tmp) > 0):
                dp[i] = max(tmp)+1
        return max(dp)
# @lc code=end

