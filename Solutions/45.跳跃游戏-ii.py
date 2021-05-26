#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# https://leetcode-cn.com/problems/jump-game-ii/description/
#
# algorithms
# Medium (39.99%)
# Likes:    989
# Dislikes: 0
# Total Accepted:    133.3K
# Total Submissions: 333K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
# 
# 假设你总是可以到达数组的最后一个位置。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 
# 
# 示例 2:
# 
# 
# 输入: [2,3,0,1,4]
# 输出: 2
# 
# 
# 
# 
# 提示:
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [float('inf')]*N
        dp[0] = 0
        for i in range(N):
            for j in range(1,nums[i]+1):
                if i+j >= N:
                    break
                dp[i+j] = min(dp[i+j], dp[i] + 1)
        return dp[N-1]
# @lc code=end

