#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#
# https://leetcode-cn.com/problems/degree-of-an-array/description/
#
# algorithms
# Easy (60.62%)
# Likes:    349
# Dislikes: 0
# Total Accepted:    62.2K
# Total Submissions: 102.6K
# Testcase Example:  '[1,2,2,3,1]'
#
# 给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。
# 
# 你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[1, 2, 2, 3, 1]
# 输出：2
# 解释：
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
# 
# 
# 示例 2：
# 
# 
# 输入：[1,2,2,3,1,4,2]
# 输出：6
# 
# 
# 
# 
# 提示：
# 
# 
# nums.length 在1到 50,000 区间范围内。
# nums[i] 是一个在 0 到 49,999 范围内的整数。
# 
# 
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic, ans = dict(), 0
        for i,n in enumerate(nums):
            if n not in dic:
                dic[n] = [i, i, 1]
            else:
                dic[n][1] = i
                dic[n][2] += 1
            if ans < dic[n][2]:
                ans = dic[n][2]

        res = float('inf')
        for k, lst in dic.items():
            if lst[2] == ans:
                res = min(res, lst[1] - lst[0] + 1)
        return res
# @lc code=end

