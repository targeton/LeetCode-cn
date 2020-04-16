#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (49.36%)
# Likes:    1188
# Dislikes: 0
# Total Accepted:    90.7K
# Total Submissions: 179.3K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res, leftMax, rightMax = 0, 0, 0
        l, r = 0, len(height)-1
        while l < r:
            if height[l] < height[r]:
                if height[l] > leftMax:
                    leftMax = height[l]
                else:
                    res += leftMax - height[l]
                l += 1
            else:
                if height[r] > rightMax:
                    rightMax = height[r]
                else:
                    res += rightMax - height[r]
                r -= 1
        return res

# @lc code=end

