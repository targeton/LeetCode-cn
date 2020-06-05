#
# @lc app=leetcode.cn id=1287 lang=python3
#
# [1287] 有序数组中出现次数超过25%的元素
#
# https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array/description/
#
# algorithms
# Easy (61.18%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    6.4K
# Total Submissions: 10.5K
# Testcase Example:  '[1,2,2,6,6,6,6,7,10]'
#
# 给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。
# 
# 请你找到并返回这个整数
# 
# 
# 
# 示例：
# 
# 
# 输入：arr = [1,2,2,6,6,6,6,7,10]
# 输出：6
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cnt, cur, N = 0, arr[0], len(arr)
        for i in range(N):
            if arr[i] == cur:
                cnt += 1
                if cnt * 4 > N:
                    return cur
            else:
                cnt, cur = 1, arr[i]
        return -1

# @lc code=end

